"""Backend da Zerésima da Urna Eletrônica.

A zerésima é emitida ANTES da votação para comprovar que a urna está vazia:
nenhum candidato com votos e nenhum eleitor marcado como "votou".

Fluxo:
    1. validar_urna()    -> confere se a urna realmente está zerada
    2. gerar_zeresima()  -> monta os dados do relatório (levanta erro se inválida)
    3. formatar_texto()  -> gera o texto no mesmo estilo do Relatório Final
    4. salvar_zeresima() -> grava o .txt (com hash SHA-256 de integridade)
"""

import hashlib
from datetime import datetime
from pathlib import Path

LARGURA = 60
LINHA = "-" * LARGURA


class ZeresimaInvalida(Exception):
    """A urna não está zerada, então a zerésima não pode ser emitida."""

    def __init__(self, erros):
        self.erros = erros
        super().__init__("; ".join(erros))


class EleicaoJaIniciada(Exception):
    """A eleição já começou (zerésima emitida ou votos computados)."""


def carregar_do_banco():
    """Devolve (candidatos, eleitores) do banco_de_dados.py.

    Candidato: {"nome", "numero_candidato", "partido", "votos", "imagem"}
    Eleitor:   {"nome", "titulo_eleitor", "votou"}
    """
    try:  
        from Backend import banco_de_dados as bd
    except ModuleNotFoundError:  
        import banco_de_dados as bd
    return bd.candidatos, bd.eleitores



def validar_urna(candidatos, eleitores):
    """Devolve uma lista de erros. Lista vazia = urna zerada e válida."""
    erros = []

    if not candidatos:
        erros.append("Nenhum candidato cadastrado.")

    numeros = [c["numero_candidato"] for c in candidatos]
    if len(numeros) != len(set(numeros)):
        erros.append("Há candidatos com número repetido.")

    for c in candidatos:
        if c["votos"] != 0:
            erros.append(f"Candidato '{c['nome']}' já possui {c['votos']} voto(s).")

    for e in eleitores:
        if e["votou"]:
            erros.append(f"Eleitor '{e['nome']}' já consta como tendo votado.")

    return erros


def gerar_zeresima(candidatos, eleitores, momento=None):
    """Valida a urna e devolve os dados da zerésima.

    Levanta ZeresimaInvalida se houver qualquer voto registrado.
    """
    erros = validar_urna(candidatos, eleitores)
    if erros:
        raise ZeresimaInvalida(erros)

    return {
        "emitido_em": momento or datetime.now(),
        "candidatos": [
            {
                "nome": str(c["nome"]),
                "numero_candidato": c["numero_candidato"],
                "votos": 0,
            }
            for c in sorted(candidatos, key=lambda c: int(c["numero_candidato"]))
        ],
        "total_eleitores": len(eleitores),
        "total_votos": 0,
    }


def _centralizar(texto):
    return texto.center(LARGURA)


def formatar_texto(zeresima):
    """Monta o texto da zerésima (mesmo visual do Relatório Final)."""
    agora = zeresima["emitido_em"]
    linhas = [
        _centralizar("ZERÉSIMA"),
        _centralizar(f"Data: {agora:%d/%m/%Y}   Hora: {agora:%H:%M:%S}"),
        LINHA,
        _centralizar("PRESIDENTE"),
        LINHA,
        f"{'Nome do candidato':<34}{'Núm.':^8}{'votos':>18}",
    ]

    for c in zeresima["candidatos"]:
        linhas.append(
            f"{c['nome'][:32]:<34}{c['numero_candidato']:^8}{'0 (0.0%)':>18}"
        )

    linhas += [
        LINHA,
        f"Eleitores aptos: {zeresima['total_eleitores']}",
        f"Total de votos apurados: {zeresima['total_votos']}",
        LINHA,
        _centralizar("URNA ZERADA - NENHUM VOTO REGISTRADO"),
        LINHA,
    ]
    return "\n".join(linhas)


def calcular_hash(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def salvar_zeresima(zeresima, pasta="relatorios"):
    """Grava a zerésima em .txt, com o hash SHA-256 no final. Devolve o Path."""
    texto = formatar_texto(zeresima)
    hash_sha = calcular_hash(texto)

    pasta = Path(pasta)
    pasta.mkdir(parents=True, exist_ok=True)
    caminho = pasta / f"zeresima_{zeresima['emitido_em']:%Y%m%d_%H%M%S}.txt"
    caminho.write_text(f"{texto}\nSHA-256: {hash_sha}\n", encoding="utf-8")
    return caminho


_eleicao_iniciada = False

MSG_JA_EMITIDA = (
    "A zerésima já foi emitida e a eleição está ativa.\n"
    "Não é possível emitir outra zerésima sem reiniciar o sistema."
)
MSG_COM_VOTOS = (
    "Já existem votos computados nesta urna.\n"
    "Não é possível emitir a zerésima sem reiniciar o sistema."
)


def eleicao_iniciada():
    """True depois que a zerésima foi emitida. A tela de votação pode usar
    isto para só liberar o voto quando a eleição estiver iniciada."""
    return _eleicao_iniciada


def emitir_zeresima(candidatos, eleitores):
    """Avalia a situação atual da urna.

    - Urna zerada e eleição ainda não iniciada: marca a eleição como iniciada
      e devolve um dicionário com os dados da zerésima (incluindo data e hora
      atuais do computador), pronto para a tela de relatório.
    - Eleição já ativa ou algum voto computado: levanta EleicaoJaIniciada.
    - Urna mal configurada (sem candidatos, números repetidos):
      levanta ZeresimaInvalida.
    """
    global _eleicao_iniciada

    if _eleicao_iniciada:
        raise EleicaoJaIniciada(MSG_JA_EMITIDA)

    ha_votos = any(c["votos"] != 0 for c in candidatos) or any(
        e["votou"] for e in eleitores
    )
    if ha_votos:
        raise EleicaoJaIniciada(MSG_COM_VOTOS)

    zeresima = gerar_zeresima(candidatos, eleitores)  
    zeresima["data"] = f"{zeresima['emitido_em']:%d/%m/%Y}"
    zeresima["hora"] = f"{zeresima['emitido_em']:%H:%M:%S}"
    zeresima["eleitores"] = eleitores

    _eleicao_iniciada = True  
    return zeresima


def solicitar_zeresima(parent, candidatos, eleitores):
    """Versão para a interface: tenta emitir a zerésima.

    - Sucesso: devolve o dicionário com os dados da zerésima.
    - Eleição já ativa / votos computados / urna inválida: mostra um popup de
      erro com a mensagem relevante e devolve None.
    """
    from PySide6.QtWidgets import QMessageBox  

    try:
        return emitir_zeresima(candidatos, eleitores)
    except EleicaoJaIniciada as erro:
        QMessageBox.critical(parent, "Zerésima não permitida", str(erro))
    except ZeresimaInvalida as erro:
        detalhes = "\n".join(f"- {e}" for e in erro.erros)
        QMessageBox.critical(
            parent, "Urna inválida", f"A zerésima não pode ser emitida:\n{detalhes}"
        )
    return None


if __name__ == "__main__":
    candidatos, eleitores = carregar_do_banco()

    for tentativa in (1, 2):
        try:
            zeresima = emitir_zeresima(candidatos, eleitores)
            print(f"Tentativa {tentativa}: emitida em {zeresima['data']} {zeresima['hora']}")
            print("Eleição iniciada?", eleicao_iniciada())
        except (EleicaoJaIniciada, ZeresimaInvalida) as erro:
            print(f"Tentativa {tentativa}: BLOQUEADA ->", str(erro).replace("\n", " "))
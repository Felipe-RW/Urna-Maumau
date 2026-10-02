"""Backend da Zerésima da Urna Eletrônica.

A zerésima é emitida ANTES da votação para comprovar que a urna está vazia:
nenhum candidato com votos, nenhum eleitor marcado como "votou" e nenhum voto registrado.
"""

import hashlib
from datetime import datetime
from pathlib import Path

largura = 60
linha_separadora = "-" * largura

# Variáveis dedicadas para armazenar os votos brancos e nulos
votos_brancos = 0
votos_nulos = 0

class ZeresimaInvalida(Exception):
    """A urna não está zerada, então a zerésima não pode ser emitida."""

    def __init__(self, erros):
        self.erros = erros
        super().__init__("; ".join(erros))


class EleicaoJaIniciada(Exception):
    """A eleição já começou (zerésima emitida ou votos computados)."""


def _banco():
    """Devolve o módulo banco_de_dados (sempre o mesmo objeto)."""
    try:
        from Backend import banco_de_dados as bd
    except ModuleNotFoundError:
        import banco_de_dados as bd
    return bd


def carregar_do_banco():
    """Devolve (candidatos, eleitores) do banco_de_dados.py."""
    bd = _banco()
    return bd.candidatos, bd.eleitores


def validar_urna(candidatos, eleitores):
    """Devolve uma lista de erros. Lista vazia = urna zerada e válida."""
    bd = _banco()
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

    if len(bd.votos_registrados) > 0:
        erros.append("Existem votos registrados na lista 'votos_registrados'.")

    return erros


def gerar_zeresima(candidatos, eleitores, momento=None):
    """Valida a urna e devolve os dados da zerésima."""
    erros = validar_urna(candidatos, eleitores)
    if erros:
        raise ZeresimaInvalida(erros)

    lista_opcoes = [
        {
            "nome": str(c["nome"]),
            "numero_candidato": str(c["numero_candidato"]),
            "votos": 0,
        }
        for c in sorted(candidatos, key=lambda x: int(x["numero_candidato"]))
    ]

    lista_opcoes.extend([
        {
            "nome": "Branco",
            "numero_candidato": "BRANCO",
            "votos": 0,
        }, 
        {
            "nome": "Nulo",
            "numero_candidato": "NULO",
            "votos": 0,
        }
    ])


    return {
        "emitido_em": momento or datetime.now(),
        "candidatos": lista_opcoes,
        "eleitores": eleitores,
        "total_eleitores": len(eleitores),
        "total_votos": 0,
        "votos_brancos": votos_brancos,
        "votos_nulos": votos_nulos,
    }


def _centralizar(texto):
    return texto.center(largura)


def formatar_texto(zeresima):
    """Monta o texto da zerésima."""
    agora = zeresima["emitido_em"]
    linhas = [
        _centralizar("ZERÉSIMA"),
        _centralizar(f"Data: {agora:%d/%m/%Y}   Hora: {agora:%H:%M:%S}"),
        linha_separadora,
        _centralizar("PRESIDENTE"),
        linha_separadora,
        f"{'Nome do candidato':<34}{'Núm.':^8}{'votos':>18}",
    ]

    for c in zeresima["candidatos"]:
        linhas.append(
            f"{c['nome'][:32]:<34}{c['numero_candidato']:^8}{'0 (0.0%)':>18}"
        )

    eleitores = zeresima.get("eleitores", [])
    linhas += [
        linha_separadora,
        _centralizar("ELEITORES APTOS"),
        linha_separadora,
        f"{'Nome':<34}{'Título':>26}",
    ]

    if eleitores:
        for eleitor in eleitores:
            nome = str(eleitor.get("nome", "Desconhecido"))[:34]
            titulo = str(eleitor.get("titulo_eleitor", "??"))
            linhas.append(f"{nome:<34}{titulo:>26}")
    else:
        linhas.append(_centralizar("Nenhum eleitor cadastrado"))

    linhas += [
        linha_separadora,
        f"Eleitores aptos: {zeresima['total_eleitores']}",
        f"Total de votos apurados: {zeresima['total_votos']}",
        linha_separadora,
        _centralizar("URNA ZERADA - NENHUM VOTO REGISTRADO"),
        linha_separadora,
    ]
    return "\n".join(linhas)


def calcular_hash(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def salvar_zeresima(zeresima, pasta_destino="relatorios"):
    """Grava a zerésima em .txt, com o hash SHA-256 no final."""
    texto_zeresima = formatar_texto(zeresima)
    hash_sha = calcular_hash(texto_zeresima)

    pasta = Path(pasta_destino)
    pasta.mkdir(parents=True, exist_ok=True)
    caminho_arquivo = pasta / f"zeresima_{zeresima['emitido_em']:%Y%m%d_%H%M%S}.txt"
    caminho_arquivo.write_text(f"{texto_zeresima}\nSHA-256: {hash_sha}\n", encoding="utf-8")
    return caminho_arquivo


msg_ja_emitida = (
    "A zerésima já foi emitida e a eleição está ativa.\n"
    "Não é possível emitir outra zerésima sem reiniciar o sistema."
)
msg_com_votos = (
    "Já existem votos computados nesta urna.\n"
    "Não é possível emitir a zerésima sem reiniciar o sistema."
)


def eleicao_iniciada():
    """Lê a flag bd.eleicao_ativa."""
    return _banco().eleicao_ativa


def emitir_zeresima(candidatos, eleitores):
    """Avalia a situação atual da urna e emite a zerésima."""
    bd = _banco()

    if bd.eleicao_ativa:
        raise EleicaoJaIniciada(msg_ja_emitida)

    ha_votos = (
        any(c["votos"] != 0 for c in candidatos) 
        or any(e["votou"] for e in eleitores) 
        or len(bd.votos_registrados) > 0
    )
    
    if ha_votos:
        raise EleicaoJaIniciada(msg_com_votos)

    zeresima = gerar_zeresima(candidatos, eleitores)
    zeresima["data"] = f"{zeresima['emitido_em']:%d/%m/%Y}"
    zeresima["hora"] = f"{zeresima['emitido_em']:%H:%M:%S}"

    bd.eleicao_ativa = True
    return zeresima


def solicitar_zeresima(parent, candidatos, eleitores):
    """Versão para a interface gráfica."""
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


class GerenciadorZeresima:
    """Coordena a emissão da zerésima e sua exibição em popup."""

    def __init__(self, parent):
        self.parent = parent

    def executar(self):
        from PySide6.QtCore import Qt
        from PySide6.QtGui import QFont
        from PySide6.QtWidgets import QMessageBox

        candidatos, eleitores = carregar_do_banco()
        zeresima = solicitar_zeresima(self.parent, candidatos, eleitores)
        if zeresima is None:
            return None

        texto = formatar_texto(zeresima)
        hash_sha = calcular_hash(texto)

        popup = QMessageBox(self.parent)
        popup.setWindowTitle("Zerésima emitida")
        popup.setTextFormat(Qt.TextFormat.PlainText)
        popup.setFont(QFont("Courier New", 10))
        popup.setText(f"{texto}\nSHA-256: {hash_sha}")
        popup.setStandardButtons(QMessageBox.StandardButton.Ok)
        popup.exec()
        return zeresima


if __name__ == "__main__":
    candidatos, eleitores = carregar_do_banco()
    
    for tentativa in (1, 2):
        try:
            zeresima = emitir_zeresima(candidatos, eleitores)
            print(f"Tentativa {tentativa}: emitida em {zeresima['data']} {zeresima['hora']}")
            print("Eleição iniciada?", eleicao_iniciada())
        except (EleicaoJaIniciada, ZeresimaInvalida) as erro:
            print(f"Tentativa {tentativa}: BLOQUEADA ->", str(erro).replace("\n", " "))
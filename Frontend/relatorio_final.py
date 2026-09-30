import sys
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QLabel, QMainWindow,
    QScrollArea, QVBoxLayout, QWidget
)

# Procure por ">>> SINCRONIZAR COM O BACKEND" para achar os pontos de ligação.

DESCONHECIDO = "Desconhecido"

ESTILO_TEXTO = "color: black; background: transparent;"
H_CENTRO = Qt.AlignmentFlag.AlignHCenter
H_DIREITA = Qt.AlignmentFlag.AlignRight
H_ESQUERDA = Qt.AlignmentFlag.AlignLeft


def fonte_mono(tamanho=11, negrito=False):
    fonte = QFont("Courier New", tamanho)
    fonte.setStyleHint(QFont.StyleHint.Monospace)
    fonte.setBold(negrito)
    return fonte


def rotulo(texto, negrito=False, alinhamento=H_ESQUERDA):
    lbl = QLabel(texto)
    lbl.setFont(fonte_mono(negrito=negrito))
    lbl.setStyleSheet(ESTILO_TEXTO)
    lbl.setAlignment(alinhamento | Qt.AlignmentFlag.AlignVCenter)
    return lbl


def linha_tracejada():
    lbl = QLabel("-" * 60)
    lbl.setFont(fonte_mono())
    lbl.setStyleSheet(ESTILO_TEXTO)
    lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return lbl


def limpar_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.hide()
            widget.setParent(None)
            widget.deleteLater()
        elif item.layout():
            limpar_layout(item.layout())


class RelatorioFinal(QMainWindow):
    """Relatório Final (somente exibição) com apuração, brancos, nulos, empate e anulação."""

    def __init__(self, lista_candidatos=None, lista_eleitores=None, votos_brancos=0, votos_nulos=0, status_eleicao="NORMAL", vencedor=None):
        super().__init__()

        # >>> SINCRONIZAR COM O BACKEND: listas e dados gerais da apuração
        self.candidatos = lista_candidatos or []
        self.eleitores = lista_eleitores or []
        self.votos_brancos = votos_brancos
        self.votos_nulos = votos_nulos
        self.status_eleicao = status_eleicao  # "ELEITO", "EMPATE", "ANULADA", "NORMAL"
        self.vencedor = vencedor  # Nome ou dados do candidato vencedor

        self.setWindowTitle("Urna Eletrônica - Relatório Final")
        self.setFixedSize(600, 720)
        self.setStyleSheet("background-color: #e6e6e6;")

        area = QScrollArea()
        area.setWidgetResizable(True)
        area.setFrameShape(QFrame.Shape.NoFrame)
        self.setCentralWidget(area)
        
        self.papel = QFrame()
        self.papel.setObjectName("papel")
        self.papel.setStyleSheet("#papel { background-color: white; border: 1px solid #999; }")
        self.papel.setFixedWidth(480)

        self.layout_papel = QVBoxLayout(self.papel)
        self.layout_papel.setContentsMargins(20, 20, 20, 20)
        self.layout_papel.setSpacing(6)

        fundo = QWidget()
        layout_fundo = QVBoxLayout(fundo)
        layout_fundo.setContentsMargins(0, 10, 0, 10)
        layout_fundo.addWidget(self.papel, alignment=H_CENTRO)
        layout_fundo.addStretch()
        area.setWidget(fundo)

        self.montarRelatorio()

    def atualizar(self, lista_candidatos, lista_eleitores, votos_brancos=0, votos_nulos=0, status_eleicao="NORMAL", vencedor=None):
        """Chame quando o backend enviar os dados finais da votação e apuração."""
        self.candidatos = lista_candidatos or []
        self.eleitores = lista_eleitores or []
        self.votos_brancos = votos_brancos
        self.votos_nulos = votos_nulos
        self.status_eleicao = status_eleicao
        self.vencedor = vencedor
        self.montarRelatorio()

    def montarRelatorio(self):
        limpar_layout(self.layout_papel)
        self.criarCabecalho()
        self.criarColunas()
        self.criarResultadoVotacao()  # Nova seção para brancos, nulos, vencedor, empate/anulação
        self.criarRodape()

    def totalVotosValidos(self):
        return sum(c.get("votos", 0) for c in self.candidatos)

    def totalVotosGerais(self):
        return self.totalVotosValidos() + self.votos_brancos + self.votos_nulos

    def porcentagemCandidato(self, votos):
        total = self.totalVotosGerais()
        return votos / total * 100 if total else 0.0

    def porcentagemBrancos(self):
        total = self.totalVotosGerais()
        return self.votos_brancos / total * 100 if total else 0.0

    def porcentagemNulos(self):
        total = self.totalVotosGerais()
        return self.votos_nulos / total * 100 if total else 0.0

    def criarCabecalho(self):
        titulo = rotulo("RELATÓRIO FINAL", negrito=True, alinhamento=H_CENTRO)
        titulo.setFont(fonte_mono(14, True))
        self.layout_papel.addWidget(titulo)

        agora = datetime.now()
        self.layout_papel.addWidget(
            rotulo(f"Data: {agora:%d/%m/%Y}   Hora: {agora:%H:%M:%S}", alinhamento=H_CENTRO)
        )
        self.layout_papel.addWidget(linha_tracejada())
        self.layout_papel.addWidget(rotulo("PRESIDENTE", negrito=True, alinhamento=H_CENTRO))
        self.layout_papel.addWidget(linha_tracejada())

    def criarColunas(self):
        colunas = QHBoxLayout()
        colunas.setSpacing(10)

        coluna1, coluna2, coluna3 = QVBoxLayout(), QVBoxLayout(), QVBoxLayout()
        for col in (coluna1, coluna2, coluna3):
            col.setSpacing(6)
            col.setAlignment(Qt.AlignmentFlag.AlignTop)
        colunas.addLayout(coluna1, 5)
        colunas.addLayout(coluna2, 2)
        colunas.addLayout(coluna3, 3)

        coluna1.addWidget(rotulo("Nome do candidato", negrito=True))
        coluna2.addWidget(rotulo("Núm.", negrito=True, alinhamento=H_CENTRO))
        coluna3.addWidget(rotulo("votos", negrito=True, alinhamento=H_DIREITA))

        if not self.candidatos:
            for _ in range(2):
                coluna1.addWidget(rotulo(DESCONHECIDO))
                coluna2.addWidget(rotulo("??", alinhamento=H_CENTRO))
                coluna3.addWidget(rotulo("0.0%", alinhamento=H_DIREITA))
        else:
            for c in self.candidatos:
                votos = c.get("votos", 0)
                pct = self.porcentagemCandidato(votos)
                coluna1.addWidget(rotulo(str(c.get("nome", DESCONHECIDO))))
                coluna2.addWidget(rotulo(f"{int(c.get('numero_candidato', 0)):02d}", alinhamento=H_CENTRO))
                coluna3.addWidget(rotulo(f"{pct:.1f}%", alinhamento=H_DIREITA))

        self.layout_papel.addLayout(colunas)

    def criarResultadoVotacao(self):
        """Adiciona contagem de Brancos, Nulos, Vencedor, Empate e Anulação."""
        self.layout_papel.addWidget(linha_tracejada())
        
        # Votos em Branco e Nulos com suas respectivas porcentagens
        pct_b = self.porcentagemBrancos()
        pct_n = self.porcentagemNulos()
        self.layout_papel.addWidget(rotulo(f"Votos em Branco: {self.votos_brancos} ({pct_b:.1f}%)"))
        self.layout_papel.addWidget(rotulo(f"Votos Nulos: {self.votos_nulos} ({pct_n:.1f}%)"))
        
        self.layout_papel.addWidget(linha_tracejada())

        # Status da Eleição / Vencedor / Empate / Anulação
        status = str(self.status_eleicao).upper()
        
        if status == "ANULADA":
            self.layout_papel.addWidget(rotulo("RESULTADO: VOTAÇÃO ANULADA", negrito=True, alinhamento=H_CENTRO))
        elif status == "EMPATE":
            self.layout_papel.addWidget(rotulo("RESULTADO: EMPATE NA ELEIÇÃO", negrito=True, alinhamento=H_CENTRO))
        elif status == "ELEITO":
            nome_vencedor = str(self.vencedor) if self.vencedor else DESCONHECIDO
            self.layout_papel.addWidget(rotulo(f"ELEITO(A): {nome_vencedor}", negrito=True, alinhamento=H_CENTRO))
        else:
            self.layout_papel.addWidget(rotulo(f"STATUS: {status}", negrito=True, alinhamento=H_CENTRO))

    def criarRodape(self):
        self.layout_papel.addWidget(linha_tracejada())
        self.layout_papel.addWidget(rotulo("Eleitores que votaram", negrito=True))
        self.layout_papel.addWidget(rotulo(f"{'Nome':<24} {'Título':>5}", negrito=True))

        quem_votou = [e for e in self.eleitores if e.get("votou", False)]
        if not quem_votou:
            self.layout_papel.addWidget(rotulo(f"{DESCONHECIDO:<24} {'??':>5}"))
        for e in quem_votou:
            nome_eleitor = str(e.get("nome", DESCONHECIDO))[:24]
            titulo_eleitor = str(e.get("titulo_eleitor", "??"))
            self.layout_papel.addWidget(rotulo(f"{nome_eleitor:<24} {titulo_eleitor:>5}"))
        
        self.layout_papel.addWidget(linha_tracejada())
        if self.eleitores:
            aptos = len(self.eleitores)
            votaram = len(quem_votou)
            abstencoes = aptos - votaram
            pct_votaram = votaram / aptos * 100 if aptos else 0.0
            pct_abst = abstencoes / aptos * 100 if aptos else 0.0
            self.layout_papel.addWidget(rotulo(f"Eleitores aptos: {aptos}"))
            self.layout_papel.addWidget(rotulo(f"Votaram: {votaram} ({pct_votaram:.1f}%)"))
            self.layout_papel.addWidget(rotulo(f"Abstenções: {abstencoes} ({pct_abst:.1f}%)"))
        else:
            self.layout_papel.addWidget(rotulo("Eleitores aptos: ??"))
            self.layout_papel.addWidget(rotulo("Votaram: ??"))
            self.layout_papel.addWidget(rotulo("Abstenções: ??"))

        self.layout_papel.addWidget(linha_tracejada())
        self.layout_papel.addWidget(rotulo("FIM DO RELATÓRIO", negrito=True, alinhamento=H_CENTRO))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Exemplo simulando dados enviados pela apuração do backend
    candidatos_exemplo = [
        {"nome": "Candidato A", "numero_candidato": 12, "votos": 15},
        {"nome": "Candidato B", "numero_candidato": 22, "votos": 10}
    ]
    eleitores_exemplo = [
        {"nome": "Eleitor Teste 1", "titulo_eleitor": "001", "votou": True},
        {"nome": "Eleitor Teste 2", "titulo_eleitor": "002", "votou": True}
    ]

    janela = RelatorioFinal(
        lista_candidatos=candidatos_exemplo,
        lista_eleitores=eleitores_exemplo,
        votos_brancos=2,
        votos_nulos=3,
        status_eleicao="ELEITO",
        vencedor="Candidato A"
    )
    janela.show()

    sys.exit(app.exec())
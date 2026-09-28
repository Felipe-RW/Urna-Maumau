#Puxar os dados dos candidatos (Nome e numero)
#Puxar os dados dos eleitores (Nome somente pois quantidade já tem)



import sys
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QLabel, QMainWindow,
    QScrollArea, QVBoxLayout, QWidget
)

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from Backend.banco_de_dados import eleitores,candidatos


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


class Zeresima(QMainWindow):
    """Zeresima (somente exibição)."""

    def __init__(self, lista_candidatos=None, lista_eleitores=None):
        super().__init__()

        # >>> SINCRONIZAR COM O BACKEND: listas de candidatos e eleitores
        # (podem vir no construtor ou pelo método atualizar()).
        self.candidatos = lista_candidatos or []
        self.eleitores = lista_eleitores or []

        self.setWindowTitle("Urna Eletrônica - Zeresima")
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

    
    def atualizar(self, lista_candidatos, lista_eleitores):
        """Chame quando o backend enviar os dados finais da votação."""
        # >>> SINCRONIZAR COM O BACKEND: o backend deve chamar este método
        # passando a lista de candidatos (com votos) e a lista de eleitores.
        self.candidatos = lista_candidatos or []
        self.eleitores = lista_eleitores or []
        self.montarRelatorio()

    def montarRelatorio(self):
        limpar_layout(self.layout_papel)
        self.criarCabecalho()
        self.criarColunas()
        self.criarRodape()

    
    def totalVotos(self):
        # >>> SINCRONIZAR COM O BACKEND: chave "votos" de cada candidato
        return sum(c["votos"] for c in self.candidatos)

    def porcentagem(self, votos):
        total = self.totalVotos()
        return votos / total * 100 if total else 0.0

    
    def criarCabecalho(self):
        titulo = rotulo("Zeresima", negrito=True, alinhamento=H_CENTRO)
        titulo.setFont(fonte_mono(14, True))
        self.layout_papel.addWidget(titulo)

        agora = datetime.now()
        self.layout_papel.addWidget(
            rotulo(f"Data: {agora:%d/%m/%Y}   Hora: {agora:%H:%M:%S}", alinhamento=H_CENTRO)
        )
        self.layout_papel.addWidget(linha_tracejada())
        self.layout_papel.addWidget(rotulo("Candidatos", negrito=True, alinhamento=H_CENTRO))
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

        

        if not self.candidatos:
            for _ in range(2):
                
                for candidatoss in candidatos:
                    self.layout_papel.addWidget(rotulo(f"{candidatoss["nome"]}", negrito=True))   
                    self.layout_papel.addWidget(rotulo(f"Número:{candidatoss["numero_candidato"]}", negrito=True))
                    self.layout_papel.addWidget(rotulo(f"{candidatoss["partido"]}", negrito=True))
                    self.layout_papel.addWidget(rotulo(f"Votos:{candidatoss["votos"]}", negrito=True))
                    self.layout_papel.addWidget(rotulo("-="*25, negrito=True))
        else:
            # >>> SINCRONIZAR COM O BACKEND: chaves "nome", "numero_candidato"
            # e "votos" de cada candidato (mesmas do banco_de_dados.py).
            for c in self.candidatos:
                pct = self.porcentagem(c["votos"])
                coluna1.addWidget(rotulo(str(c["nome"])))
                coluna2.addWidget(rotulo(f"{c['numero_candidato']:02d}", alinhamento=H_CENTRO))
                coluna3.addWidget(rotulo(f"{pct:.1f}%", alinhamento=H_DIREITA))
                

        self.layout_papel.addLayout(colunas)
        

    
    def criarRodape(self):
        
        self.layout_papel.addWidget(linha_tracejada())
        self.layout_papel.addWidget(rotulo("Eleitores", negrito=True, alinhamento=H_CENTRO))
        self.layout_papel.addWidget(linha_tracejada())
        

        for eleitor in eleitores:
            self.layout_papel.addWidget(rotulo(f"{eleitor["nome"]}", negrito=True))

        # >>> SINCRONIZAR COM O BACKEND: chaves "votou", "nome" e
        # "titulo_eleitor" de cada eleitor (mesmas do banco_de_dados.py).
        quem_votou = [e for e in self.eleitores if e["votou"]]
        if not quem_votou:
            self.layout_papel.addWidget(rotulo(f""))
        for e in quem_votou:
            self.layout_papel.addWidget(rotulo(f"{str(e['nome'])[:24]:<24} {e['titulo_eleitor']:>5}"))
   
        if self.eleitores:
            aptos = len(self.eleitores)
            votaram = len(quem_votou)
            nulos = aptos - votaram
            pct_votaram = votaram / aptos * 100
            pct_abst = nulos / aptos * 100
            self.layout_papel.addWidget(rotulo(f"Eleitores aptos: {aptos}"))
            self.layout_papel.addWidget(rotulo(f"Votaram: {votaram} ({pct_votaram:.1f}%)"))
            self.layout_papel.addWidget(rotulo(f"Nulos: {nulos} ({pct_abst:.1f}%)"))
        else:
            self.layout_papel.addWidget(rotulo(f"Eleitores aptos: {len(eleitores)}"))
            self.layout_papel.addWidget(rotulo("Votaram: 0"))
            self.layout_papel.addWidget(rotulo("Nulos: 0"))

        self.layout_papel.addWidget(linha_tracejada())
        self.layout_papel.addWidget(rotulo("Nenhuma Votação ENCONTRADA!", negrito=True))

        self.layout_papel.addWidget(linha_tracejada())
        self.layout_papel.addWidget(rotulo("FIM DO RELATÓRIO", negrito=True, alinhamento=H_CENTRO))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quantidade = QLabel(str(len(eleitores)))

    # >>> SINCRONIZAR COM O BACKEND: sem dados, os campos ficam "Desconhecido"
    # até o backend chamar janela.atualizar(candidatos, eleitores).
    janela = Zeresima()
    janela.show()

    sys.exit(app.exec())
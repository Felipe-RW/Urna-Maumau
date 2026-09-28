import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFrame,
    QLabel,
    QPushButton
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class UrnaEletronica(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Urna Eletrônica - PySide6")
        self.setFixedSize(1408, 860)

        self.tela = QWidget()
        self.tela.setStyleSheet("background-color: #f0f0f0;")
        self.setCentralWidget(self.tela)

        self.criar_painel_esquerdo()
        self.criar_painel_direito()

    def criar_painel_esquerdo(self):

       
        self.painel_esquerdo = QFrame(self.tela)
        self.painel_esquerdo.setGeometry(30, 28, 782, 754)
        self.painel_esquerdo.setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border: 2px solid #b8b8b8;
                border-radius: 6px;
            }
        """)

        
        self.titulo = QLabel("PRESIDENTE", self.painel_esquerdo)
        self.titulo.setGeometry(30, 30, 718, 45)

        self.titulo.setFont(QFont("Arial", 25, QFont.Weight.Bold))
        self.titulo.setAlignment(
            Qt.AlignmentFlag.AlignVCenter |
            Qt.AlignmentFlag.AlignLeft
        )

        self.titulo.setStyleSheet("""
            QLabel {
                background-color: #eeeeee;
                color: #111111;
                border: 2px solid #b8b8b8;
                border-radius: 5px;
                padding-left: 10px;
            }
        """)

        
        self.numero_1 = QLabel("", self.painel_esquerdo)
        self.numero_1.setGeometry(30, 114, 60, 75)
        self.numero_1.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid #222222;
                border-radius: 5px;
            }
        """)

        
        self.numero_2 = QLabel("", self.painel_esquerdo)
        self.numero_2.setGeometry(98, 114, 60, 75)
        self.numero_2.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid #222222;
                border-radius: 5px;
            }
        """)

      
        self.campo_informacao = QLabel("", self.painel_esquerdo)
        self.campo_informacao.setGeometry(30, 226, 718, 38)
        self.campo_informacao.setStyleSheet("""
            QLabel {
                background-color: #eeeeee;
                border: 2px solid #b8b8b8;
                border-radius: 5px;
            }
        """)

     
        self.instrucoes = QLabel(
            "Aperte a tecla:\n"
            "VERDE para CONFIRMAR\n"
            "LARANJA para CORRIGIR",
            self.painel_esquerdo
        )

        self.instrucoes.setGeometry(30, 647, 718, 73)
        self.instrucoes.setFont(QFont("Arial", 15))

        self.instrucoes.setAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter
        )

        self.instrucoes.setStyleSheet("""
            QLabel {
                background-color: #eeeeee;
                color: #222222;
                border: 2px solid #b8b8b8;
                border-radius: 5px;
                padding-left: 5px;
            }
        """)

    def criar_painel_direito(self):

        
        self.painel_direito = QFrame(self.tela)
        self.painel_direito.setGeometry(856, 28, 520, 754)

        self.painel_direito.setStyleSheet("""
            QFrame {
                background-color: #white;
                border: 2px solid #111111;
                border-radius: 10px;
            }
        """)

        
        


if __name__ == "__main__":

    app = QApplication(sys.argv)

    janela = UrnaEletronica()
    janela.show()

    sys.exit(app.exec())
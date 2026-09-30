
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFrame,
    QLabel,
    QPushButton,
    QLineEdit
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class UrnaEletronica(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Urna Eletrônica - PySide6")
        self.setFixedSize(1280, 720)

        self.tela = QWidget()
        self.tela.setStyleSheet("background-color: #f0f0f0;")
        self.setCentralWidget(self.tela)

        self.criar_painel_esquerdo()
        self.criar_painel_direito()

    def criar_painel_esquerdo(self):

       
        self.painel_esquerdo = QFrame(self.tela)
        self.painel_esquerdo.setGeometry(25, 24, 710, 672)
        self.painel_esquerdo.setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border: 2px solid #b8b8b8;
                border-radius: 6px;
            }
        """)

        
        self.titulo = QLabel("PRESIDENTE", self.painel_esquerdo)
        self.titulo.setGeometry(27, 27, 652, 40)

        self.titulo.setFont(QFont("Arial", 23, QFont.Weight.Bold))
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

        
        self.numero_1 = QLineEdit(self.painel_esquerdo)
        self.numero_1.setGeometry(27, 102, 55, 68)
        self.numero_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.numero_1.setMaxLength(1)
        self.numero_1.setFont(QFont("Arial", 32, QFont.Weight.Bold))
        self.numero_1.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #111111;
                border: 2px solid #222222;
                border-radius: 5px;
            }
        """)

        
        self.numero_2 = QLineEdit(self.painel_esquerdo)
        self.numero_2.setGeometry(89, 102, 55, 68)
        self.numero_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.numero_2.setMaxLength(1)
        self.numero_2.setFont(QFont("Arial", 32, QFont.Weight.Bold))
        self.numero_2.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #111111;
                border: 2px solid #222222;
                border-radius: 5px;
            }
        """)

      
        self.campo_informacao = QLabel("", self.painel_esquerdo)
        self.campo_informacao.setGeometry(27, 202, 652, 35)
        self.campo_informacao.setStyleSheet("""
            QLabel {
                background-color: #eeeeee;
                border: 2px solid #b8b8b8;
                border-radius: 5px;
            }
        """)

              
        self.foto_candidato = QFrame(self.painel_esquerdo)
        self.foto_candidato.setGeometry(400, 255, 250, 300)

        self.foto_candidato.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #222222;
                border-radius: 5px;
            }
        """)

     
        self.instrucoes = QLabel(
            "Aperte a tecla:\n"
            "VERDE para CONFIRMAR\n"
            "LARANJA para CORRIGIR",
            self.painel_esquerdo
        )

        self.instrucoes.setGeometry(27, 577, 652, 65)
        self.instrucoes.setFont(QFont("Arial", 14))

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
        self.painel_direito.setGeometry(775, 24, 480, 672)

        self.painel_direito.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 2px solid #111111;
                border-radius: 10px;
            }
        """)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    janela = UrnaEletronica()
    janela.show()

    sys.exit(app.exec())



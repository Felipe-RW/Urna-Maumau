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

from painel_numerico import TecladoUrna


class UrnaEletronica(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Urna Eletrônica - PySide6")
        self.setFixedSize(1280, 720)

        self.tela = QWidget()
        self.tela.setObjectName("telaPrincipal")

        self.tela.setStyleSheet("""
            QWidget#telaPrincipal {
                background-color: #f0f0f0;
            }
        """)

        self.setCentralWidget(self.tela)

        self.criar_painel_esquerdo()
        self.criar_painel_direito()


    def criar_painel_esquerdo(self):

        self.painel_esquerdo = QFrame(
            self.tela
        )

        self.painel_esquerdo.setGeometry(
            25, 24, 710, 672
        )

        self.painel_esquerdo.setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border: 2px solid #b8b8b8;
                border-radius: 6px;
            }
        """)


        self.titulo = QLabel(
            "PRESIDENTE",
            self.painel_esquerdo
        )

        self.titulo.setGeometry(
            27, 27, 652, 40
        )

        self.titulo.setFont(
            QFont(
                "Arial",
                23,
                QFont.Weight.Bold
            )
        )

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


        self.numero_1 = QLabel(
            self.painel_esquerdo
        )

        self.numero_1.setGeometry(
            27, 102, 55, 68
        )

        self.numero_1.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.numero_1.setFont(
            QFont(
                "Arial",
                32,
                QFont.Weight.Bold
            )
        )

        self.numero_1.setStyleSheet("""
            QLabel {
                background-color: white;
                color: #111111;
                border: 2px solid #222222;
                border-radius: 5px;
            }
        """)


        self.numero_2 = QLabel(
            self.painel_esquerdo
        )

        self.numero_2.setGeometry(
            89, 102, 55, 68
        )

        self.numero_2.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.numero_2.setFont(
            QFont(
                "Arial",
                32,
                QFont.Weight.Bold
            )
        )

        self.numero_2.setStyleSheet("""
            QLabel {
                background-color: white;
                color: #111111;
                border: 2px solid #222222;
                border-radius: 5px;
            }
        """)


        self.campo_informacao = QLabel(
            "",
            self.painel_esquerdo
        )

        self.campo_informacao.setGeometry(
            27, 202, 652, 35
        )

        self.campo_informacao.setStyleSheet("""
            QLabel {
                background-color: #eeeeee;
                border: 2px solid #b8b8b8;
                border-radius: 5px;
            }
        """)


        self.foto_candidato = QFrame(
            self.painel_esquerdo
        )

        self.foto_candidato.setGeometry(
            400, 255, 250, 300
        )

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

        self.instrucoes.setGeometry(
            27, 577, 652, 65
        )

        self.instrucoes.setFont(
            QFont("Arial", 14)
        )

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

        self.painel_direito = QFrame(
            self.tela
        )

        self.painel_direito.setGeometry(
            815, 10, 404, 704
        )

        self.painel_direito.setObjectName(
            "painelDireito"
        )

        self.painel_direito.setStyleSheet("""
            QFrame#painelDireito {
                background-color: #ffffff;
                border: 2px solid #111111;
                border-radius: 10px;
            }
        """)


        self.teclado = TecladoUrna(
            self.painel_direito
        )

        self.teclado.move(
            2, 2
        )


        self.teclado.acaoNumero = (
            self.receber_numero
        )

        self.teclado.acaoCorrigir = (
            self.corrigir_numero
        )


    def receber_numero(self, numero):

        if self.numero_1.text() == "":
            self.numero_1.setText(
                numero
            )

        elif self.numero_2.text() == "":
            self.numero_2.setText(
                numero
            )


    def corrigir_numero(self):

        self.numero_1.setText("")
        self.numero_2.setText("")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    janela = UrnaEletronica()

    janela.show()

    sys.exit(app.exec())
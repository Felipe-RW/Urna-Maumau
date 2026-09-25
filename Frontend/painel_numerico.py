import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton
)


class TecladoUrna(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Teclado Urna")
        self.setFixedSize(450, 720)

        self.setStyleSheet("""
            background-color: #2b2b2b;
            border-radius: 8px;
        """)

        self.criarTeclado()


    def criarTeclado(self):

        self.labelJusticaEleitoral = QLabel("Justiça Eleitoral", self)
        self.labelJusticaEleitoral.setGeometry(30, 20, 390, 130)
        self.labelJusticaEleitoral.setAlignment(Qt.AlignCenter)

        self.labelJusticaEleitoral.setStyleSheet("""
            background-color: #252525;
            border-radius: 5px;
            color: white;
            border: 2px solid #202020;
            font-size: 20px;
            font-weight: bold;
        """)

        self.botoesNumericos = []

        numeros = [
            ("1", 70, 180),
            ("2", 185, 180),
            ("3", 300, 180),

            ("4", 70, 260),
            ("5", 185, 260),
            ("6", 300, 260),

            ("7", 70, 340),
            ("8", 185, 340),
            ("9", 300, 340),

            ("0", 185, 420)
        ]

        for numero, x, y in numeros:

            btnNumero = QPushButton(numero, self)
            btnNumero.setGeometry(x, y, 80, 60)

            btnNumero.setStyleSheet("""
                QPushButton {
                    background-color: #1f1f1f;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    font-size: 24px;
                    font-weight: bold;
                }

                QPushButton:hover {
                    background-color: #383838;
                }

                QPushButton:pressed {
                    background-color: #111111;
                }
            """)

            self.botoesNumericos.append(btnNumero)

        self.btnBranco = QPushButton("BRANCO", self)
        self.btnBranco.setGeometry(30, 550, 110, 60)

        self.btnBranco.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                border: none;
                border-radius: 4px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #eeeeee;
            }

            QPushButton:pressed {
                background-color: #cccccc;
            }
        """)

        self.btnCorrige = QPushButton("CORRIGE", self)
        self.btnCorrige.setGeometry(165, 550, 110, 60)

        self.btnCorrige.setStyleSheet("""
            QPushButton {
                background-color: #ff7f27;
                color: black;
                border: none;
                border-radius: 4px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #ff934d;
            }

            QPushButton:pressed {
                background-color: #dd650f;
            }
        """)

        self.btnConfirma = QPushButton("CONFIRMA", self)
        self.btnConfirma.setGeometry(300, 550, 110, 60)

        self.btnConfirma.setStyleSheet("""
            QPushButton {
                background-color: #32cd32;
                color: black;
                border: none;
                border-radius: 4px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #45df45;
            }

            QPushButton:pressed {
                background-color: #28a428;
            }
        """)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    janela = TecladoUrna()
    janela.show()

    sys.exit(app.exec())
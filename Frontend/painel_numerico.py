import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton
)

#a
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

        self.label_justica_eleitoral = QLabel("Justiça Eleitoral", self)
        self.label_justica_eleitoral.setGeometry(30, 20, 390, 130)
        self.label_justica_eleitoral.setAlignment(Qt.AlignCenter)

        self.label_justica_eleitoral.setStyleSheet("""
            background-color: #252525;
            border-radius: 5px;
            color: white;
            border: 2px solid #202020;
            font-size: 20px;
            font-weight: bold;
        """)

        self.botoes_numericos = []

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

            btn_numero = QPushButton(numero, self)
            btn_numero.setGeometry(x, y, 80, 60)

            btn_numero.setStyleSheet("""
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

            self.botoes_numericos.append(btn_numero)

        self.btn_branco = QPushButton("BRANCO", self)
        self.btn_branco.setGeometry(30, 550, 110, 60)

        self.btn_branco.setStyleSheet("""
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

        self.btn_corrige = QPushButton("CORRIGE", self)
        self.btn_corrige.setGeometry(165, 550, 110, 60)

        self.btn_corrige.setStyleSheet("""
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

        self.btn_confirma = QPushButton("CONFIRMA", self)
        self.btn_confirma.setGeometry(300, 550, 110, 60)

        self.btn_confirma.setStyleSheet("""
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
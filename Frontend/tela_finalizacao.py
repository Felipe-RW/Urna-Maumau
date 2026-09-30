import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

root_dir = Path(__file__).resolve()
sys.path.append(str(root_dir))

from tela_principal_urna import TelaPrincipalUrna


class TelaFinalizacao(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Votação")
        self.setFixedSize(500, 300)

        self.label_mensagem = QLabel(
            "VOTAÇÃO FINALIZADA!",
            self
        )

        self.label_mensagem.setAlignment(Qt.AlignCenter)
        self.label_mensagem.setGeometry(0, 0, 500, 300)

    def voltarMenu(self):
        self.tela_principal = TelaPrincipalUrna()
        self.tela_principal.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    tela = TelaFinalizacao()
    tela.show()

    sys.exit(app.exec())
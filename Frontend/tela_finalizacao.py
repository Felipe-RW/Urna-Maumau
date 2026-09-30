import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from tela_principal_urna import TelaPrincipalUrna


class TelaFinalizacao(QMainWindow):

  def __init__(self):
    super().__init__()

    self.setWindowTitle("Urna Eletrônica - Justiça Eleitoral")
    self.setFixedSize(1280, 720)
    self.setStyleSheet("background-color: white;")

    # Widget central
    c_widget = QWidget()
    self.setCentralWidget(c_widget)

    # Layout principal
    top_level_layout = QVBoxLayout()
    top_level_layout.setContentsMargins(0, 0, 0, 20)
    c_widget.setLayout(top_level_layout)

    # CABEÇALHO
    topo_layout = QHBoxLayout()
    topo_layout.setContentsMargins(20, 10, 20, 0)
    topo_layout.setAlignment(
        Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop
    )

    self.btn_sair = QPushButton("Sair")
    self.btn_sair.setFixedSize(100, 35)

    self.btn_sair.setStyleSheet("""
            QPushButton {
                font-size: 12px;
                font-weight: bold;
                font-family: 'Verdana';
                background-color: #d32f2f;
                color: white;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #b71c1c;
            }
        """)

    self.btn_sair.clicked.connect(self.close)

    topo_layout.addWidget(self.btn_sair)
    top_level_layout.addLayout(topo_layout)

    # Adiciona um espaçador para empurrar o conteúdo para o meio exato da tela
    top_level_layout.addStretch()

    # CONTEÚDO CENTRAL
    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # MENSAGEM
    self.label_mensagem = QLabel("VOTAÇÃO FINALIZADA!")
    self.label_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.label_mensagem.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                font-family: 'Verdana';
                color: black;
            }
        """)

    main_layout.addWidget(self.label_mensagem)

    main_layout.addSpacing(25)

    # BOTÃO VOLTAR AO MENU
    self.btn_voltar = QPushButton("Voltar ao Menu")
    self.btn_voltar.setFixedSize(260, 45)

    self.btn_voltar.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                font-family: 'Verdana';
                background-color: #f0f0f0;
                color: black;
                border: 1px solid #cccccc;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #e0e0e0;
                border-color: #999999;
            }

            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)

    self.btn_voltar.clicked.connect(self.voltarAoMenu)

    main_layout.addWidget(
        self.btn_voltar, alignment=Qt.AlignmentFlag.AlignCenter
    )

    top_level_layout.addLayout(main_layout)

    # Espaçador inferior para manter o equilíbrio vertical
    top_level_layout.addStretch()

  def voltarAoMenu(self):
    self.tela_principal = TelaPrincipalUrna()
    self.tela_principal.show()
    self.close()


if __name__ == "__main__":
  app = QApplication(sys.argv)

  tela = TelaFinalizacao()
  tela.show()

  sys.exit(app.exec())
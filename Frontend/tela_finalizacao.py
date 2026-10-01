# import sys
# from pathlib import Path


# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QSizePolicy,
#     QSpacerItem,
#     QVBoxLayout,
#     QWidget,

# )

# from PySide6.QtMultimedia import QSoundEffect
# from PySide6.QtCore import QUrl




# root_dir = Path(__file__).resolve().parent.parent
# sys.path.insert(0, str(root_dir))

# from tela_principal_urna import TelaPrincipalUrna


# class TelaFinalizacao(QMainWindow):

#   def __init__(self):
#     super().__init__()

#     self.setWindowTitle("Urna Eletrônica - Justiça Eleitoral")
#     self.setFixedSize(1280, 720)
#     self.setStyleSheet("background-color: white;")

#     c_widget = QWidget()
#     self.setCentralWidget(c_widget)

#     # Layout principal centralizado
#     top_level_layout = QVBoxLayout(c_widget)
#     top_level_layout.setContentsMargins(0, 0, 0, 0)
#     top_level_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

#     # Conteúdo do meio
#     main_layout = QVBoxLayout()
#     main_layout.setContentsMargins(0, 0, 0, 0)
#     main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

#     self.label_mensagem = QLabel("VOTAÇÃO ENCERRADA!")
#     self.label_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
#     self.label_mensagem.setStyleSheet("""
#             QLabel {
#                 font-size: 28px;
#                 font-weight: bold;
#                 font-family: 'Verdana';
#                 color: black;
#             }
#         """)
#     main_layout.addWidget(self.label_mensagem)

#     main_layout.addSpacing(25)

#     self.btn_voltar = QPushButton("Voltar ao Menu")
#     self.btn_voltar.setFixedSize(260, 45)
#     self.btn_voltar.setStyleSheet("""
#             QPushButton {
#                 font-size: 14px;
#                 font-weight: bold;
#                 font-family: 'Verdana';
#                 background-color: #f0f0f0;
#                 color: black;
#                 border: 1px solid #cccccc;
#                 border-radius: 6px;
#             }
#             QPushButton:hover {
#                 background-color: #e0e0e0;
#                 border-color: #999999;
#             }
#             QPushButton:pressed {
#                 background-color: #d0d0d0;
#             }
#         """)
#     self.btn_voltar.clicked.connect(self.voltarAoMenu)
#     main_layout.addWidget(
#         self.btn_voltar, alignment=Qt.AlignmentFlag.AlignCenter
#     )

#     top_level_layout.addLayout(main_layout)

#   def voltarAoMenu(self):
#     self.tela_principal = TelaPrincipalUrna()
#     self.tela_principal.show()
#     self.close()


# # Caso esteja tudo de acordo, o arquivo será executado pela "tela_principal_urna"
# if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   tela = TelaFinalizacao()
#   tela.show()
#   sys.exit(app.exec())





import sys
from pathlib import Path


from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,

)

from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl


root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from tela_principal_urna import TelaPrincipalUrna


class TelaFinalizacao(QMainWindow):

  def __init__(self):
    super().__init__()

    
    self.som_confirmacao = QSoundEffect()
    self.som_confirmacao.setSource(
        QUrl.fromLocalFile(
            str(Path(__file__).resolve().parent / "sons" / "confirma-urna.wav")
        )
    )
    self.som_confirmacao.setVolume(1.0)
    self.som_confirmacao.play()

    self.setWindowTitle("Urna Eletrônica - Justiça Eleitoral")
    self.setFixedSize(1280, 720)
    self.setStyleSheet("background-color: white;")

    c_widget = QWidget()
    self.setCentralWidget(c_widget)

    # Layout principal centralizado
    top_level_layout = QVBoxLayout(c_widget)
    top_level_layout.setContentsMargins(0, 0, 0, 0)
    top_level_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.label_mensagem = QLabel("VOTAÇÃO ENCERRADA!")
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

  def voltarAoMenu(self):
    self.tela_principal = TelaPrincipalUrna()
    self.tela_principal.show()
    self.close()


# Caso esteja tudo de acordo, o arquivo será executado pela "tela_principal_urna"
if __name__ == "__main__":
  app = QApplication(sys.argv)
  tela = TelaFinalizacao()
  tela.show()
  sys.exit(app.exec())
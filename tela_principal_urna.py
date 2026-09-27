import sys
import os

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QLabel, QPushButton
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

# IMPORTS FUTUROS (Comentados até que as telas do Frontend/Backend existam)

	# from Frontend.tela_zeresima import TelaZeresima
	# from Backend.urna import Urna


class TelaPrincipalUrna(QMainWindow):  
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Urna Eletrônica - Justiça Eleitoral")
        

        self.setFixedSize(1280, 720)


        self.setStyleSheet("background-color: white;")
        c_widget = QWidget()
        self.setCentralWidget(c_widget)


        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        c_widget.setLayout(main_layout)

        self.lbl_logo = QLabel()
        caminho_imagem = os.path.join("Imagens", "JusticaEleitoral.png")
        

        pixmap = QPixmap(caminho_imagem)
        self.lbl_logo.setPixmap(pixmap.scaledToWidth(300, Qt.TransformationMode.SmoothTransformation))
        self.lbl_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.lbl_logo)


        main_layout.addSpacing(25)


        self.lbl_mensagem = QLabel("Clique para tirar a zerésima")
        self.lbl_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lbl_mensagem.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
        main_layout.addWidget(self.lbl_mensagem)


        main_layout.addSpacing(25)

# BOTÃO ZERÉSIMA

        botoes_layout = QHBoxLayout()
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn_zeresima = QPushButton("Tirar Zerésima")
        self.btn_zeresima.setFixedSize(220, 45)
# Estilização visual básica do botão
        self.btn_zeresima.setStyleSheet("font-size: 14px; font-weight: bold;")
        
        
        self.btn_zeresima.clicked.connect(self.gerarZeresima)
        botoes_layout.addWidget(self.btn_zeresima)

        main_layout.addLayout(botoes_layout)


    def gerarZeresima(self):

        print("Ação: Gerando a Zerésima...")
        
#LÓGICA DE TRANSIÇÃO FUTURA 
        # self.urna = Urna()
        # self.urna.gerarZeresima()
        
        
        # self.proxima_tela = TelaZeresima()
        # self.proxima_tela.show()
        # self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = TelaPrincipalUrna()
    window.show()
    
    sys.exit(app.exec())

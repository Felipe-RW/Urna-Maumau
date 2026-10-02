import sys
import os
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QDialog,
    QMessageBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

base_dir=Path(__file__).resolve().parent

from Backend import gerar_zeresima as backend_zeresima
from Backend import banco_de_dados
from Backend.apurar_resultados import ApurarResultado
from Frontend.relatorio_final import RelatorioFinal


class TelaPrincipalUrna(QMainWindow):  
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Urna Eletrônica - Justiça Eleitoral")
        self.setFixedSize(1280, 720)
        self.setStyleSheet("background-color: white;")

        # Widget central
        c_widget = QWidget()
        self.setCentralWidget(c_widget)

        # Layout principal sem margens superiores
        top_level_layout = QVBoxLayout()
        top_level_layout.setContentsMargins(0, 0, 0, 20)
        c_widget.setLayout(top_level_layout)

        # CABEÇALHO (Botão Sair posicionado no canto superior direito)
        topo_layout = QHBoxLayout()
        topo_layout.setContentsMargins(20, 10, 20, 0)
        topo_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        self.btn_sair = QPushButton("Sair")
        self.btn_sair.setFixedSize(100, 35)
        self.btn_sair.setStyleSheet("""
            QPushButton {
                font-size: 12px;
                font-weight: bold;
                background-color: #d32f2f;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #b71c1c;
            }
        """)
        self.btn_sair.clicked.connect(self.sairApp)
        topo_layout.addWidget(self.btn_sair)

        top_level_layout.addLayout(topo_layout)

        # LAYOUT PRINCIPAL DO CONTEÚDO
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        # IMAGEM NO TOPO
        self.lbl_logo = QLabel()
        caminho_imagem = os.path.join(base_dir, "Imagens", "LogoJusticaEleitoral.jpg")
        
        if os.path.exists(caminho_imagem):
            pixmap = QPixmap(caminho_imagem)
            self.lbl_logo.setPixmap(pixmap.scaled(
                600, 320,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            self.lbl_logo.setText("[Imagem do Brasão]")
            
        self.lbl_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.lbl_logo)

        main_layout.addSpacing(10)

        # MENSAGEM
        self.lbl_mensagem = QLabel("Urna Eletrônica \n [versão:10.24.0.0]")
        self.lbl_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_mensagem.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
        main_layout.addWidget(self.lbl_mensagem)

        main_layout.addSpacing(15)

        # BOTÕES CENTRAIS
        botoes_centro_layout = QVBoxLayout()
        botoes_centro_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        botoes_centro_layout.setSpacing(12)

        # Estilo padrão para os botões brancos com efeito Hover
        estilo_botao_branco = """
            QPushButton {
                font-size: 14px;
                font-weight: bold;
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
        """

        # BOTÃO 1: ZERÉSIMA
        self.btn_zeresima = QPushButton("Tirar Zerésima")
        self.btn_zeresima.setFixedSize(260, 45)
        self.btn_zeresima.setStyleSheet(estilo_botao_branco)
        self.btn_zeresima.clicked.connect(self.gerarZeresima)
        botoes_centro_layout.addWidget(self.btn_zeresima)

        # BOTÃO 2: APURAR RESULTADO
        self.btn_apurar_resultado = QPushButton("Apurar Resultado")
        self.btn_apurar_resultado.setFixedSize(260, 45)
        self.btn_apurar_resultado.setStyleSheet(estilo_botao_branco)
        self.btn_apurar_resultado.clicked.connect(self.apurarResultado)
        botoes_centro_layout.addWidget(self.btn_apurar_resultado)

        # BOTÃO 3: VOTAÇÃO
        self.btn_votacao = QPushButton("Votação")
        self.btn_votacao.setFixedSize(260, 45)
        self.btn_votacao.setStyleSheet(estilo_botao_branco)
        self.btn_votacao.clicked.connect(self.iniciarVotacao)
        botoes_centro_layout.addWidget(self.btn_votacao)

        main_layout.addLayout(botoes_centro_layout)

        top_level_layout.addLayout(main_layout)

        # Espaçador final
        top_level_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    def gerarZeresima(self):
        backend_zeresima.GerenciadorZeresima(self).executar()

    def apurarResultado(self):
        resultado = ApurarResultado(
            candidatos=banco_de_dados.candidatos,
            eleitores=banco_de_dados.eleitores,
            votos_brancos=banco_de_dados.votos_brancos,
            votos_nulos=banco_de_dados.votos_nulos,
            eleicao_aberta=banco_de_dados.eleicao_ativa,
        ).apurarResultado()

        if resultado is None:
            QMessageBox.warning(
                self,
                "Apuração indisponível",
                "A eleição ainda não foi iniciada.",
            )
            return

        banco_de_dados.eleicao_ativa = False
        situacoes_relatorio = {
            "Eleição anulada": "ANULADA",
            "Empate": "EMPATE",
            "Eleição finalizada": "ELEITO",
            "Sem votos válidos": "SEM VOTOS VÁLIDOS",
        }
        vencedor = resultado["vencedor"]

        self.relatorio_final = RelatorioFinal(
            lista_candidatos=resultado["candidatos"],
            lista_eleitores=resultado["eleitores"],
            votos_brancos=resultado["votos_brancos"],
            votos_nulos=resultado["votos_nulos"],
            status_eleicao=situacoes_relatorio[resultado["situacao"]],
            vencedor=vencedor["nome"] if vencedor else None,
        )
        self.relatorio_final.show()

    def iniciarVotacao(self):
        if not banco_de_dados.eleicao_ativa:
            QMessageBox.warning(
                self,
                "Zerésima obrigatória",
                "Emita a zerésima antes de iniciar a votação.",
            )
            return

        print("Ação: Carregando Tela de Votação...")
        # Importação Local para evitar Circular Import
        from Frontend.pop_up_titulo_eleitor import PopUpInserirTituloEleitor
        from Frontend.tela_votacao import UrnaEletronica

        popup = PopUpInserirTituloEleitor(self)
        resultado = popup.exec()

        if resultado == QDialog.Accepted:
            titulo_validado = popup.transformar_str()
            print(f"Título Aprovado: {titulo_validado}. Abrindo votação...")
            abrir_votacao = UrnaEletronica(eleitor=popup.eleitor_validado)
            abrir_votacao.show()
            self.close()




        else:
            print("Operação cancelada pelo usuário. Permanecendo na Tela Principal.")

    def sairApp(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = TelaPrincipalUrna()
    window.show()
    
    sys.exit(app.exec())
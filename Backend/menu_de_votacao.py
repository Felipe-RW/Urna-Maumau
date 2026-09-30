import sys
import os
from pathlib import Path

# Adiciona o diretório pai (raiz do projeto) ao sys.path para garantir que o Python encontre os módulos do projeto
DIRETORIO_RAIZ = Path(__file__).resolve().parent.parent
if str(DIRETORIO_RAIZ) not in sys.path:
    sys.path.append(str(DIRETORIO_RAIZ))

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


from banco_de_dados import candidatos, eleitores
from confirmar_voto import ConfirmarVotos
from cancelar_voto import CancelarVoto


class TelaVotacao(QWidget):
    def __init__(self, titulo_eleitor):
        super().__init__()

        self.titulo_eleitor = titulo_eleitor
        self.candidato_atual = None


        self.eleitor_atual = None
        for eleitor in eleitores:
            if eleitor["titulo_eleitor"] == titulo_eleitor:
                self.eleitor_atual = eleitor
                break



        self.setWindowTitle("Urna Eletrônica - Votação")
        self.setFixedSize(1280, 720)
        self.setStyleSheet("background-color: white;")

        layout_principal = QHBoxLayout()
        layout_principal.setContentsMargins(40, 40, 40, 40)
        layout_principal.setSpacing(30)




        painel_dados = QVBoxLayout()
        painel_dados.setAlignment(Qt.AlignmentFlag.AlignTop)

        lbl_titulo = QLabel("Seu Voto Vai Para:")
        lbl_titulo.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: #333;"
        )
        painel_dados.addWidget(lbl_titulo)



        self.lbl_foto = QLabel()
        self.lbl_foto.setFixedSize(200, 250)
        self.lbl_foto.setFrameShape(QFrame.Shape.Box)
        self.lbl_foto.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_foto.setStyleSheet(
            "border: 2px solid #ccc; background-color: #f9f9f9;"
        )
        self.lbl_foto.setText("Sem foto")
        painel_dados.addWidget(self.lbl_foto)




        self.lbl_nome = QLabel("Nome: -")
        self.lbl_nome.setStyleSheet(
            "font-size: 20px; font-weight: bold; margin-top: 10px;"
        )
        painel_dados.addWidget(self.lbl_nome)




        self.lbl_partido = QLabel("Partido: -")
        self.lbl_partido.setStyleSheet(
            "font-size: 18px; color: #555;"
        )
        painel_dados.addWidget(self.lbl_partido)

        layout_principal.addLayout(painel_dados, stretch=2)




        painel_controles = QVBoxLayout()
        painel_controles.setAlignment(Qt.AlignmentFlag.AlignCenter)
        painel_controles.setSpacing(20)



        lbl_instrucao = QLabel("Digite o número do candidato:")
        lbl_instrucao.setStyleSheet(
            "font-size: 18px; font-weight: bold;"
        )
        lbl_instrucao.setAlignment(Qt.AlignmentFlag.AlignCenter)
        painel_controles.addWidget(lbl_instrucao)



        self.input_numero = QLineEdit()
        self.input_numero.setMaxLength(5)
        self.input_numero.setFixedSize(250, 50)
        self.input_numero.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_numero.setStyleSheet(
            "font-size: 24px; font-weight: bold; letter-spacing: 5px;"
        )
        self.input_numero.textChanged.connect(self.buscarCandidato)
        painel_controles.addWidget(self.input_numero)



        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(15)




        self.btn_cancelar = QPushButton("CORRIGE / CANCELAR")
        self.btn_cancelar.setFixedSize(180, 50)
        self.btn_cancelar.setStyleSheet("""
            QPushButton {
                background-color: #d32f2f;
                color: white;
                font-weight: bold;
                font-size: 14px;
                border-radius: 5px;
            }
        """)
        self.btn_cancelar.clicked.connect(self.acaoCancelar)
        botoes_layout.addWidget(self.btn_cancelar)


        self.btn_confirmar = QPushButton("CONFIRMAR")
        self.btn_confirmar.setFixedSize(180, 50)
        self.btn_confirmar.setStyleSheet("""
            QPushButton {
                background-color: #388e3c;
                color: white;
                font-weight: bold;
                font-size: 14px;
                border-radius: 5px;
            }
        """)
        self.btn_confirmar.clicked.connect(self.acaoConfirmar)
        botoes_layout.addWidget(self.btn_confirmar)

        painel_controles.addLayout(botoes_layout)
        layout_principal.addLayout(painel_controles, stretch=3)

        self.setLayout(layout_principal)



    def buscarCandidato(self, numero):
        if not numero:
            self.lbl_nome.setText("Nome: -")
            self.lbl_partido.setText("Partido: -")
            self.lbl_foto.clear()
            self.lbl_foto.setText("Sem foto")
            self.candidato_atual = None
            return

        dados = None
        for candidato in candidatos:
            if str(candidato["numero_candidato"]) == str(numero):
                dados = candidato
                break

        if dados:
            self.candidato_atual = dados
            self.lbl_nome.setText(f"Nome: {dados['nome']}")
            self.lbl_partido.setText(f"Partido: {dados['partido']}")

            caminho_img = str(dados["imagem"])
            if os.path.exists(caminho_img):
                pixmap = QPixmap(caminho_img)
                self.lbl_foto.setPixmap(
                    pixmap.scaled(
                        200,
                        250,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                )
            else:
                self.lbl_foto.clear()
                self.lbl_foto.setText("Foto não encontrada")
        else:
            self.candidato_atual = None
            self.lbl_nome.setText("Nome: CANDIDATO INEXISTENTE")
            self.lbl_partido.setText("Partido: ")
            self.lbl_foto.clear()
            self.lbl_foto.setText("VOTO NULO")



    def acaoConfirmar(self):
        numero = self.input_numero.text().strip()

        if not numero:
            QMessageBox.warning(
                self,
                "Aviso",
                "Digite o número antes de confirmar"
            )
            return

        if self.eleitor_atual is None:
            QMessageBox.critical(
                self,
                "Erro",
                "Eleitor não encontrado."
            )
            return

        confirmar_voto = ConfirmarVotos(candidatos, eleitores)
        confirmar_voto.submeterVotos(self.titulo_eleitor, numero)

        QMessageBox.information(
            self,
            "FIM",
            "Voto gravado com sucesso."
        )
        self.limparCampos()
        self.close()

    def acaoCancelar(self):
        if self.eleitor_atual is None:
            QMessageBox.critical(
                self,
                "Erro",
                "Eleitor não encontrado."
            )
            return

        cancelar_voto = CancelarVoto(self.eleitor_atual)
        resultado = cancelar_voto.cancelarVoto(self.titulo_eleitor)

        if resultado:
            self.limparCampos()

    def limparCampos(self):
        self.input_numero.clear()
        self.lbl_nome.setText("Nome: -")
        self.lbl_partido.setText("Partido: -")
        self.lbl_foto.clear()
        self.lbl_foto.setText("Sem foto")
        self.candidato_atual = None
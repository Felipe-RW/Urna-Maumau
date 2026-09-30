import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, 
    QHBoxLayout, QLabel, QLineEdit, QPushButton
)
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt, QTimer

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
if str(RAIZ_PROJETO) not in sys.path:
    sys.path.append(str(RAIZ_PROJETO))

from Backend.validar_eleitor import ValidarEleitor
from Frontend.urna import UrnaEletronica
from tela_principal_urna import TelaPrincipalUrna

class PopUpInserirTituloEleitor(QDialog):
    def __init__(self, parent=None, title="Justiça Eleitoral", texto_de_instrucao="Insira o número do seu título:"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(300)

        layout = QVBoxLayout(self)

        self.subtitulo = QLabel(texto_de_instrucao)
        layout.addWidget(self.subtitulo)

        self.titulo_eleitor = QLineEdit()
        self.titulo_eleitor.setPlaceholderText("Apenas números...")
        
        validador = QIntValidator(0, 999999999, self)
        self.titulo_eleitor.setValidator(validador)
        layout.addWidget(self.titulo_eleitor)

        self.label_erro = QLabel("")
        self.label_erro.setStyleSheet("color: red;")
        layout.addWidget(self.label_erro)

        layout_botao = QHBoxLayout()
        self.botao_cancelar = QPushButton("Cancelar")
        self.botao_confirmar = QPushButton("Confirmar")
        self.botao_confirmar.setDefault(True)

        layout_botao.addWidget(self.botao_cancelar)
        layout_botao.addWidget(self.botao_confirmar)
        layout.addLayout(layout_botao)

        self.botao_confirmar.clicked.connect(self.validar_e_confirmar)
        self.botao_cancelar.clicked.connect(self.reject)

    def transformar_str(self) -> str:
        return self.titulo_eleitor.text().strip()

    def validar_e_confirmar(self):
        """Valida o título no Backend antes de fechar o popup."""
        titulo = self.transformar_str()

        if not titulo:
            self.label_erro.setText("Digite o número do título.")
            return

        backend = ValidarEleitor()
        eh_valido = backend.validarEleitor(titulo)

        if eh_valido:
            self.accept()
        else:
            self.label_erro.setText("Título de eleitor inválido!")
    


class AbrirPopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Urna Eletrônica")
        self.setGeometry(100, 100, 400, 150)

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(0, self.executar_fluxo_eleitor)

    def executar_fluxo_eleitor(self):
        popup = PopUpInserirTituloEleitor(self)
        resultado = popup.exec()

        if resultado == QDialog.Accepted:
            titulo_digitado = popup.transformar_str()
            print(f"Título aprovado: {titulo_digitado}.")
            
            try:  
                self.close()
            

                
            except AttributeError:
                print("Erro: Verifique se o nome da classe em 'tela_principal_urna.py' é 'TelaPrincipalUrna'.")
            except Exception as e:
                print(f"Erro ao abrir a janela da urna: {e}")
        else:
            print("Operação cancelada pelo utilizador.")
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AbrirPopUp()
    janela.show()
    sys.exit(app.exec())
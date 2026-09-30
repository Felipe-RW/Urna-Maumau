import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, 
    QHBoxLayout, QLabel, QLineEdit, QPushButton
)
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt


class PopUpInserirTituloEleitor(QDialog):
    def __init__(self, parent=None, title="Informe apenas números", texto_de_instrução="Insira o número do seu título:"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(300)

        layout = QVBoxLayout(self)

        self.subtitulo = QLabel(texto_de_instrução)
        layout.addWidget(self.subtitulo)

        self.texto_placehoder = QLineEdit()
        self.texto_placehoder.setPlaceholderText("Apenas números...")
        
        validador = QIntValidator(0, 999999999, self)
        self.texto_placehoder.setValidator(validador)
        
        layout.addWidget(self.texto_placehoder)

        layout_botao = QHBoxLayout()

        self.botao_cancelar = QPushButton("Cancelar")
        self.botao_confirmar = QPushButton("Confirmar")
        self.botao_confirmar.setDefault(True)  # Ativa ao pressionar Enter

        layout_botao.addWidget(self.botao_cancelar)
        layout_botao.addWidget(self.botao_confirmar)
        layout.addLayout(layout_botao)

        self.botao_confirmar.clicked.connect(self.accept)
        self.botao_cancelar.clicked.connect(self.reject)

    def transformar_str(self) -> str:
        return self.texto_placehoder.text()


class AbrirPopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Confirmar ou Cancelar - Teste")
        self.setGeometry(100, 100, 400, 150)

        layout = QVBoxLayout()

        self.resultado_confirmar = QLabel("Aguardando ação...")
        layout.addWidget(self.resultado_confirmar, alignment=Qt.AlignCenter)
        container = QDialog()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def showEvent(self, event):
        """Abre o popup automaticamente ao exibir a janela principal."""
        super().showEvent(event)
        self.open_number_dialog()

    def open_number_dialog(self):
        dialog = PopUpInserirTituloEleitor(self, title="Justiça Eleitoral", texto_de_instrução="Insira o número do seu título:")
        result = dialog.exec()

        if result == QDialog.Accepted:
            self.resultado_confirmar.setText(f"Resultado: Confirmado")
        else:
            self.resultado_confirmar.setText("Resultado: Cancelado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AbrirPopUp()
    window.show()
    sys.exit(app.exec())
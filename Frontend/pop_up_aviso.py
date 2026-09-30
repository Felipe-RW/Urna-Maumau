import sys
from PySide6.QtWidgets import QApplication, QMessageBox


class PopUpAviso(QMessageBox):

    def popupConfirmacao(self, mensagem):
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Aviso")
        self.setText(mensagem)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        self.button(QMessageBox.Yes).setText("Sim")
        self.button(QMessageBox.No).setText("Não")

        resposta = self.exec()

        if resposta == QMessageBox.Yes:
            # Aqui o usuário confirma a ação.
            pass

        elif resposta == QMessageBox.No:
            # Aqui o usuário cancela a ação.
            pass

    # popup utilizado para informar um erro
    def popUp_erro(self, mensagem="Ocorreu um erro."):
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle("Erro!")
        self.setText(mensagem)
        self.setStandardButtons(QMessageBox.Ok)
        self.exec()


app = QApplication(sys.argv)

pop_up = PopUpAviso()
pop_up.popupConfirmacao("Deseja confirmar voto?")

sys.exit(app.exec())

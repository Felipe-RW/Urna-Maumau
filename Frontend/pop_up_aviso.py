import sys
from PySide6.QtWidgets import QApplication, QMessageBox


class PopUp_aviso(QMessageBox):

    def popUp_confirmacao(self):
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Confirmar voto")
        self.setText("Deseja confirmar voto?")
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        self.button(QMessageBox.Yes).setText("Confirmar")
        self.button(QMessageBox.No).setText("Cancelar")

        resposta = self.exec()

        if resposta == QMessageBox.Yes:
            # Aqui se a mensagem for "sim" o usuário vai ser enviado para a próxima tela.
            pass

        elif resposta == QMessageBox.No:
            # Se caso o usuário marcar como "não" ele irá voltar a página inicial.
            pass

    def popUp_erro(self, mensagem="Ocorreu um erro."):
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle("Erro!")
        self.setText(mensagem)
        self.setStandardButtons(QMessageBox.Ok)
        self.exec()


app = QApplication(sys.argv)

popup = PopUp_aviso()
popup.popUp_confirmacao()

sys.exit(app.exec())
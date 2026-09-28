import sys
from PySide6.QtWidgets import QApplication, QMessageBox


class PopUp(QMessageBox):
    def popUp_cancelamento(self):
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Cancelar voto")
        self.setText("Deseja cancelar seu voto?\nO que foi digitado será apagado.")
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.button(QMessageBox.Yes).setText("Sim")
        self.button(QMessageBox.No).setText("Não")
        return self.exec() == QMessageBox.Yes


class Votacao:
    def __init__(self):
        self.digitos = ""
        self.candidato = None
        self.acesso_liberado = False  # só vira True quando o eleitor confirmar o voto

    def reiniciarVotacao(self):
        # volta ao começo do processo de votação, sem salvar nada
        self.digitos = ""
        self.candidato = None
        # TODO: atualizar a tela para o início da votação (não o menu)

    def cancelarVoto(self):
        popup = PopUp()
        if popup.popUp_cancelamento():
            self.reiniciarVotacao()
            return True
        return False  # eleitor desistiu de cancelar, segue de onde estava


app = QApplication(sys.argv)

votacao = Votacao()
votacao.digitos = "13"
votacao.cancelarVoto()

sys.exit(app.exec())
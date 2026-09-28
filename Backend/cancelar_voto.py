from PySide6.QtWidgets import QMessageBox


class CancelamentoVoto:
    def __init__(self, eleitor):
        self.eleitor = eleitor  # -> dicionário da lista eleitores
        self.digitos = ""    # -> informações digitadas pelo eleitor na votação
        self.acesso_liberado = False  # -> só libera quando o eleitor confirmar o voto

    def cancelarVoto(self):
        popup = QMessageBox()
        popup.setIcon(QMessageBox.Warning)
        popup.setWindowTitle("Cancelar voto")
        popup.setText("Deseja cancelar seu voto?")
        popup.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        popup.button(QMessageBox.Yes).setText("Sim")
        popup.button(QMessageBox.No).setText("Não")

        resposta = popup.exec()

        if resposta == QMessageBox.Yes:
            # reinicia o processo de votação daquele eleitor,
            # sem salvar as informações digitadas anteriormente
            self.digitos = ""
            self.eleitor["votou"] = False

            # não volta ao menu, volta ao começo do processo de votação

            return True

        # clicou em "não", segue de onde parou
        return False
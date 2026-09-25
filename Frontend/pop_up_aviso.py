import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

msg = QMessageBox()
msg.setIcon(QMessageBox.Warning)
msg.setWindowTitle("Confirmar voto")
msg.setText("Deseja confirmar voto?")
msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
msg.button(QMessageBox.Yes).setText("Confirmar")
msg.button(QMessageBox.No).setText("Cancelar")

resposta = msg.exec()

sys.exit(app.exec())
#Pop-Up de aviso de confirmar voto finalizado.
import sys
from pathlib import Path
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from Backend.banco_de_dados import candidatos

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Path Example")

        print(candidatos)
        image_path = candidatos[0]['imagem']
   
        label = QLabel(self)
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print("Failed to load image.")
        label.setPixmap(pixmap)
        
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
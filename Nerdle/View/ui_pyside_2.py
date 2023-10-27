from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QLabel
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Novia.")
        self.resize(480, 320)

        etiqueta = QLabel("Soy una etiqueta.")
        fuente = etiqueta.font()
        fuente.setPointSize(10)
        etiqueta.setFont(fuente)

        self.setCentralWidget(etiqueta)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

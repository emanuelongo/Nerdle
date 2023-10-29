from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        radial = QRadioButton("Botón radial")

        self.setCentralWidget(radial)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QGridLayout, QLabel, QLineEdit, QWidget, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.container = QFrame()
        self.container.setStyleSheet("QFrame{background-color: yellow}")
        # Declaramos un grid Layout
        self.grid = QGridLayout()
        # Widgets
        self.titulo = QLabel("Nerdle")
        self.boton_probar = QPushButton("Probar")
        self.boton_probar.setFixedSize(150, 70)
        self.boton_probar.clicked.connect(self.probar_boton)

        # Definimos la primera fila de 8 elementos.
        self.caja_1 = QLineEdit()
        # Definimos cantidad de elementos que admite cada QLine
        self.caja_1.setMaxLength(1)
        self.caja_2 = QLineEdit()
        self.caja_2.setMaxLength(1)
        self.caja_3 = QLineEdit()
        self.caja_3.setMaxLength(1)
        self.caja_4 = QLineEdit()
        self.caja_4.setMaxLength(1)
        self.caja_5 = QLineEdit()
        self.caja_5.setMaxLength(1)
        self.caja_6 = QLineEdit()
        self.caja_6.setMaxLength(1)
        self.caja_7 = QLineEdit()
        self.caja_7.setMaxLength(1)
        self.caja_8 = QLineEdit()
        self.caja_8.setMaxLength(1)

        # Definimos la segunda fila de 8 elementos.
        self.caja_9 = QLineEdit()
        # Definimos cantidad de elementos que admite cada QLine
        self.caja_9.setMaxLength(1)
        self.caja_10 = QLineEdit()
        self.caja_10.setMaxLength(1)
        self.caja_11 = QLineEdit()
        self.caja_11.setMaxLength(1)
        self.caja_12 = QLineEdit()
        self.caja_12.setMaxLength(1)
        self.caja_13 = QLineEdit()
        self.caja_13.setMaxLength(1)
        self.caja_14 = QLineEdit()
        self.caja_14.setMaxLength(1)
        self.caja_15 = QLineEdit()
        self.caja_15.setMaxLength(1)
        self.caja_16 = QLineEdit()
        self.caja_16.setMaxLength(1)

        # Definimos la tercera fila de 8 elementos.
        self.caja_17 = QLineEdit()
        # Definimos cantidad de elementos que admite cada QLine
        self.caja_17.setMaxLength(1)
        self.caja_18 = QLineEdit()
        self.caja_18.setMaxLength(1)
        self.caja_19 = QLineEdit()
        self.caja_19.setMaxLength(1)
        self.caja_20 = QLineEdit()
        self.caja_20.setMaxLength(1)
        self.caja_21 = QLineEdit()
        self.caja_21.setMaxLength(1)
        self.caja_22 = QLineEdit()
        self.caja_22.setMaxLength(1)
        self.caja_23 = QLineEdit()
        self.caja_23.setMaxLength(1)
        self.caja_24 = QLineEdit()
        self.caja_24.setMaxLength(1)

        # Definimos la cuarta fila de 8 elementos.
        self.caja_25 = QLineEdit()
        # Definimos cantidad de elementos que admite cada QLine
        self.caja_25.setMaxLength(1)
        self.caja_26 = QLineEdit()
        self.caja_26.setMaxLength(1)
        self.caja_27 = QLineEdit()
        self.caja_27.setMaxLength(1)
        self.caja_28 = QLineEdit()
        self.caja_28.setMaxLength(1)
        self.caja_29 = QLineEdit()
        self.caja_29.setMaxLength(1)
        self.caja_30 = QLineEdit()
        self.caja_30.setMaxLength(1)
        self.caja_31 = QLineEdit()
        self.caja_31.setMaxLength(1)
        self.caja_32 = QLineEdit()
        self.caja_32.setMaxLength(1)

        # Definimos la quinta fila de 8 elementos.
        self.caja_33 = QLineEdit()
        # Definimos cantidad de elementos que admite cada QLine
        self.caja_33.setMaxLength(1)
        self.caja_34 = QLineEdit()
        self.caja_34.setMaxLength(1)
        self.caja_35 = QLineEdit()
        self.caja_35.setMaxLength(1)
        self.caja_36 = QLineEdit()
        self.caja_36.setMaxLength(1)
        self.caja_37 = QLineEdit()
        self.caja_37.setMaxLength(1)
        self.caja_38 = QLineEdit()
        self.caja_38.setMaxLength(1)
        self.caja_39 = QLineEdit()
        self.caja_39.setMaxLength(1)
        self.caja_40 = QLineEdit()
        self.caja_40.setMaxLength(1)

        # Definimos la sexta fila de 8 elementos.
        self.caja_41 = QLineEdit()
        # Definimos cantidad de elementos que admite cada QLine
        self.caja_41.setMaxLength(1)
        self.caja_42 = QLineEdit()
        self.caja_42.setMaxLength(1)
        self.caja_43 = QLineEdit()
        self.caja_43.setMaxLength(1)
        self.caja_44 = QLineEdit()
        self.caja_44.setMaxLength(1)
        self.caja_45 = QLineEdit()
        self.caja_45.setMaxLength(1)
        self.caja_46 = QLineEdit()
        self.caja_46.setMaxLength(1)
        self.caja_47 = QLineEdit()
        self.caja_47.setMaxLength(1)
        self.caja_48 = QLineEdit()
        self.caja_48.setMaxLength(1)

        # Agregamos los widgets de la fila 1
        self.grid.addWidget(self.titulo, 0, 3, 1, 2, Qt.AlignCenter)
        self.grid.addWidget(self.caja_1, 1, 0, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_2, 1, 1, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_3, 1, 2, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_4, 1, 3, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_5, 1, 4, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_6, 1, 5, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_7, 1, 6, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_8, 1, 7, 1, 1, Qt.AlignCenter)

        # Agregamos los widgets de la fila 2
        self.grid.addWidget(self.caja_9, 2, 0, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_10, 2, 1, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_11, 2, 2, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_12, 2, 3, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_13, 2, 4, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_14, 2, 5, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_15, 2, 6, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_16, 2, 7, 1, 1, Qt.AlignCenter)

        # Agregamos los widgets de la fila 3
        self.grid.addWidget(self.caja_17, 3, 0, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_18, 3, 1, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_19, 3, 2, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_20, 3, 3, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_21, 3, 4, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_22, 3, 5, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_23, 3, 6, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_24, 3, 7, 1, 1, Qt.AlignCenter)

        # Agregamos los widgets de la fila 4
        self.grid.addWidget(self.caja_25, 4, 0, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_26, 4, 1, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_27, 4, 2, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_28, 4, 3, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_29, 4, 4, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_30, 4, 5, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_31, 4, 6, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_32, 4, 7, 1, 1, Qt.AlignCenter)

        # Agregamos los widgets de la fila 5
        self.grid.addWidget(self.caja_33, 5, 0, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_34, 5, 1, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_35, 5, 2, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_36, 5, 3, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_37, 5, 4, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_38, 5, 5, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_39, 5, 6, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_40, 5, 7, 1, 1, Qt.AlignCenter)

        # Agregamos los widgets de la fila 6
        self.grid.addWidget(self.caja_41, 6, 0, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_42, 6, 1, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_43, 6, 2, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_44, 6, 3, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_45, 6, 4, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_46, 6, 5, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_47, 6, 6, 1, 1, Qt.AlignCenter)
        self.grid.addWidget(self.caja_48, 6, 7, 1, 1, Qt.AlignCenter)

        self.grid.addWidget(self.boton_probar, 7, 3, 2, 2, Qt.AlignCenter)
        # Hacemos que los Widgets estén en el Layout
        self.container.setLayout(self.grid)
        # Centramos el Layout
        self.setCentralWidget(self.container)

    # Estoy acá intentando lograr que se me pinten los cuadros.
    def probar_boton(self):
        if int(self.caja_1.text()) == 1:
            self.caja_1.setStyleSheet("QLineEdit{color: red}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

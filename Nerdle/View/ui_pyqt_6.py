import sys, random
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.boton_probar = None
        self.boton_reiniciar = None
        self.mensaje_para_usuario = None
        self.tituloLabel = None
        self.caja_de_texto_de_usuarios = None
        self.titulo = "Nerdle App"
        self.left = 50
        self.top = 50
        self.ancho = 600
        self.altura = 500
        self.icono = "Icono Nerdle.png"
        self.fila_actual = 0
        self.numero_adivinar = ""
        self.ui_interface()

    def ui_interface(self):
        self.setGeometry(self.left, self.top, self.ancho, self.altura)
        self.setWindowTitle(self.titulo)
        self.setWindowIcon(QIcon(QPixmap("Icono Nerdle.png")))
        self.get_random_number()
        grid = QGridLayout()
        grid .setRowMinimumHeight(0, 30)
        grid.setRowMinimumHeight(6, 30)
        grid.setColumnMinimumWidth(0, 30)
        grid.setColumnMinimumWidth(8, 30)
        self.setStyleSheet("""
        background: "yellow";
        """)
        self.setLayout(grid)

        # Agregamos título
        self.tituloLabel = QLabel("Nerdle App")
        self.tituloLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("""
        font-size: 40px;
        font-weight: bold;
        margin: 30 px 30px 30px 30px;
        """)
        grid.addWidget(self.tituloLabel, 0, 0, 1, 7)

        self.caja_de_texto_de_usuarios = [[] for _ in range(8)]

        posiciones = [(i + 1, j + 1) for i in range(6) for j in range(8)]
        for i, posiciones in enumerate(posiciones):
            self.caja_de_texto_de_usuarios[posiciones[0]-1].append(QLineEdit())
            grid.addWidget(self.caja_de_texto_de_usuarios[posiciones[0]-1][posiciones[1]-1], *posiciones)

        for i, fila in enumerate(self.caja_de_texto_de_usuarios):
            for caja_de_usuario in fila:
                caja_de_usuario.setMaxLength(1)
                caja_de_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
                caja_de_usuario.setMinimumWidth(70)
                caja_de_usuario.setMinimumHeight(70)
                caja_de_usuario.setStyleSheet("""
                border: 2px solid '#000000';
                margin: 10px 10px 10px 10px;
                font-size: 30px;
                background: "white";
                """)
                if i != self.fila_actual:
                    caja_de_usuario.setReadOnly(True)
                    caja_de_usuario.setStyleSheet("""
                    border: 2px solid '#000000';
                    margin: 10px 10px 10px 10px;
                    font-size: 30px;
                    background: 'Light grey';
                    """)

        # Mensaje para usuario
        self.mensaje_para_usuario = QLabel("")
        self.mensaje_para_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mensaje_para_usuario.setStyleSheet("""
        font-size: 16px
        """)
        grid.addWidget(self.mensaje_para_usuario, 8, 0, 1, 8)

        # botón reiniciar
        self.boton_reiniciar = QPushButton("Reiniciar")
        self.boton_reiniciar.setStyleSheet("""
        *{
        border: 2px solid '#000000';
        font-weight: bold;
        font-size: 20px;
        margin: 0px 0px 30px 0px;
        color: 'black';
        background: 'purple';
        }
        *:hover{
        background: 'dark purple';
        color: 'white';
        }
        """)
        self.boton_reiniciar.clicked.connect(self.boton_reiniciar_clicked)
        grid.addWidget(self.boton_reiniciar, 8, 2, 1, 3)
        self.boton_reiniciar.hide()

        # Boton probar
        self.boton_probar = QPushButton("Probar")
        self.boton_probar.setStyleSheet("""
                *{
                border: 2px solid '#000000';
                font-weight: bold;
                font-size: 20px;
                margin: 0px 0px 30px 0px;
                color: 'black';
                background: 'purple';
                }
                *:hover{
                background: 'dark purple';
                color: 'white';
                }
                """)
        self.boton_probar.clicked.connect(self.boton_probar_click)
        grid.addWidget(self.boton_probar, 8, 2, 1, 3)
        self.boton_reiniciar.hide()

    def get_random_number(self):
        numbersFile = open("operaciones.txt", "r")
        numbers = numbersFile.read().splitlines()
        numbersFile.close()
        self.numero_adivinar = random.choice(numbers)

    def boton_reiniciar_clicked(self):
        self.get_random_number()
        self.fila_actual = 0
        self.mensaje_para_usuario = " "
        for i, row in enumerate(self.caja_de_texto_de_usuarios):
            for userBox in row:
                userBox.setStyleSheet("""
                border: 2px solid '#000000';
                font-size: 30px
                background: 'white';
                margin: 10px 10px 10px 10px;
                """)
                userBox.setReadOnly(False)
                userBox.setText("")
                if i != self.fila_actual:
                    userBox.setReadOnly(True)
                    userBox.setStyleSheet("""
                    border: 2px solid '#000000';
                    font-size: 30px;
                    background: 10px 10px 10px 10px;
                    """)
        self.boton_snap()

    def boton_probar_click(self):
        if not self.controlar_entradas_validas():
            self.mensaje_para_usuario.setText("Por favor ingresa solo números u operadores.")
            self.mensaje_para_usuario.repaint()
        if not self.chequear_ganador():
            self.mensaje_para_usuario.setText(" ")
            self.mensaje_para_usuario.repaint()
            if self.fila_actual < 5:
                self.activar_color_fila()
                self.activar_siguiente_fila()
            else:
                self.activar_color_fila()
                self.gameover()

    def gameover(self):
        self.mensaje_para_usuario.setText(f"¡PERDISTE! La operación era {self.numero_adivinar}")
        self.mensaje_para_usuario.repaint()
        self.boton_snap()

    def activar_color_fila(self):
        for i in range(8):
            self.caja_de_texto_de_usuarios[self.fila_actual][i].setReadOnly(True)
            valor_caja = self.caja_de_texto_de_usuarios[self.fila_actual][i].text()
            if valor_caja == self.numero_adivinar[i]:
                self.caja_de_texto_de_usuarios[self.fila_actual][i].setStyleSheet("""
                border: 2px solid '#000000';
                font-size: 30px;
                margin: 10px 10px 10px 10px;
                background: 'green';
                """)
            elif valor_caja in self.numero_adivinar:
                self.caja_de_texto_de_usuarios[self.fila_actual][i].setStyleSheet("""
                border: 2px solid '#000000';
                font-size: 30px;
                margin: 10px 10px 10px 10px;
                background: 'yellow';
                """)
            else:
                self.caja_de_texto_de_usuarios[self.fila_actual][i].setStyleSheet("""
                border: 2px solid '#000000';
                font-size: 30px;
                margin: 10px 10px 10px 10px;
                background: 'dark grey';
                """)

    def activar_siguiente_fila(self):
        for i in range(8):
            self.caja_de_texto_de_usuarios[self.fila_actual + 1][i].setStyleSheet("""
            border: 2px solid '#000000';
            font-size: 30px;
            margin: 10px 10px 10px 10px;
            background: 'white
            """)
            self.caja_de_texto_de_usuarios[self.fila_actual + 1][i].setReadOnly(False)
        self.fila_actual += 1

    def chequear_ganador(self):
        win = False
        fila_numero_actual = ""
        for i in self.caja_de_texto_de_usuarios[self.fila_actual]:
            fila_numero_actual += i.text()
        if fila_numero_actual == self.numero_adivinar:
            win = True
            for i in self.caja_de_texto_de_usuarios[self.fila_actual]:
                i.setStyleSheet("""
                border: 2px solid '#000000';
                font-size: 30px;
                background: "green";
                """)
                i.setReadOnly(True)
            self.mensaje_para_usuario.setText("¡¡¡Ganaste!!!")
            self.mensaje_para_usuario.repaint()
            self.boton_snap()
        return win

    def boton_snap(self):
        if self.boton_probar.isVisible():
            self.boton_probar.hide()
            self.boton_reiniciar.show()
        else:
            self.boton_reiniciar.hide()
            self.boton_probar.show()

    def controlar_entradas_validas(self):
        valido = True
        for i in self.caja_de_texto_de_usuarios[self.fila_actual]:
            if not i.text().isalpha():
                valido = False
        return valido


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

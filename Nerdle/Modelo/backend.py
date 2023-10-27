class Nerdle:
    def __init__(self):
        pass

    def retroalimentar(self):
        pass


class Jugador:
    intentos = 0
    repetir = True
    adivinanza = "3+50+2=5"
    decision = True

    def __init__(self):
        self.numero_de_intentos: int = int(input("¿Cuántos intentos quieres tener? (6 a 8): "))
        self.tablero = []
        while self.repetir:
            if 5 < self.numero_de_intentos < 9:
                for i in range(self.numero_de_intentos):
                    self.tablero.append(["_" for i in range(8)])
                for i in range(self.numero_de_intentos):
                    print(" ".join(self.tablero[i]))

            else:
                print("Debe ingresar un número de intentos válidos (6 a 8).")
                Jugador()
            self.repetir = False
            self.adivinar_secuencia()

    def adivinar_secuencia(self):
        print("")
        while self.intentos <= len(self.tablero):
            operacion = input("¿Cuál es tu adivinanza de 8 elementos?: ")
            print("")
            while self.decision:
                if len(operacion) == len(self.adivinanza):
                    self.intentos += 1
                    self.tablero.insert(self.intentos - 1, [operacion])
                    for i in range(self.numero_de_intentos):
                        print(" ".join(self.tablero[i]))
                    if (self.numero_de_intentos - self.intentos) == 1:
                        print("")
                        print(f"Ánimo, te queda {self.numero_de_intentos - self.intentos} intento.")
                        print("")
                    elif (self.numero_de_intentos - self.intentos) > 1 and operacion[::] != self.adivinanza[::]:
                        print("")
                        print(f"Ánimo, te quedan {self.numero_de_intentos - self.intentos} intentos.")
                        print("")
                    if operacion[::] == self.adivinanza[::] and self.intentos == 1:
                        print("")
                        print(f"Felicidades, has ganado en {self.intentos} intento.")
                        print(f"La operación era: {self.adivinanza}")
                        self.iniciar_nuevo_juego()
                        self.decision = False
                    elif operacion[::] == self.adivinanza[::] and self.intentos != 1:
                        print("")
                        print(f"Felicidades, has ganado en {self.intentos} intentos.")
                        print(f"La operación era: {self.adivinanza}")
                        self.iniciar_nuevo_juego()
                        self.decision = False
                    elif operacion[::] != self.adivinanza[::] and self.intentos == self.numero_de_intentos:
                        print("")
                        print(f"Has perdido en {self.intentos} intento.")
                        print(f"La operación era: {self.adivinanza}")
                        self.iniciar_nuevo_juego()
                        self.decision = False
                    else:
                        for operador in operacion[::]:
                            for operar in self.adivinanza[::]:
                                if operador == operar:
                                    print(f"Tienes el {operador} encontrado.")
                                else:
                                    continue
                    self.adivinar_secuencia()
                else:
                    print(f"La adivinanza debe tener {len(self.adivinanza)} elementos.")
                    print("")
                break

    def iniciar_nuevo_juego(self):
        print("")
        mensaje_antes_de_salir = int(input("Ingresa 1 para seguir jugando o 2 para salir del juego: "))
        if mensaje_antes_de_salir == 1:
            Jugador()
        elif mensaje_antes_de_salir == 2:
            self.terminar_juego()

    def terminar_juego(self):
        while self.intentos <= self.numero_de_intentos:
            print(f"Gracias por jugar, vuelve pronto.")
            break


jugador = Jugador()


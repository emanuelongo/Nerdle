class Nerdle:
    def __init__(self, secuencia):
        pass

    def generar_elemento(self):
        pass

    def mostrar_secuencia(self):
        pass

    def mostrar_intentos_restantes(self):
        pass

    def reducir_intentos(self):
        pass

    def retroalimentar(self):
        pass

    def volver_a_jugar(self):
        pass

    def terminar_juego(self):
        pass


class Jugador:
    intentos = 0
    repetir = True
    adivinanza = "3+50+2=5"
    decision = True
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.tablero = []
        while self.repetir:
            if 5 < cantidad < 9:
                for i in range(cantidad):
                    self.tablero.append(["_" for i in range(8)])
                for i in range(cantidad):
                    print(" ".join(self.tablero[i]))

            else:
                print("Debe ingresar un número de intentos válidos (6 a 8).")
                self.numero_de_intentos = int(input("¿Cuántos intentos quieres tener?: "))
                Jugador(self.numero_de_intentos)
            self.repetir = False
            self.adivinar_secuencia()

    def adivinar_secuencia(self):
        print("")
        while self.intentos <= len(self.tablero):
            operacion = input("¿Cuál es tu adivinanza de 8 elementos?: ")
            while self.decision:
                if len(operacion) == len(self.adivinanza):
                    self.intentos += 1
                    self.tablero.insert(self.intentos, [operacion])
                    for i in range(6):
                        print(" ".join(self.tablero[i]))
                    if operacion[::] == self.adivinanza[::]:
                        print(f"Felicidades, has ganado en {self.intentos} intentos.")
                        self.decision = False
                        self.iniciar_nuevo_juego()
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
                    self.intentos += 1
                    break



    def secuencia_no_adivinada(self):
        pass

    def iniciar_nuevo_juego(self):
        pass


numero_de_intentos = int(input("¿Cuántos intentos quieres tener?: "))
jugador = Jugador(numero_de_intentos)


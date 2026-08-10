import time
import random

class Celda:

    def __init__(self, columna:int, fila:int, valor:str, naufrago:bool = False):
        self.columna = columna
        self.fila = fila
        self.valor = valor
        self.naufrago = naufrago

    def __str__(self):
        return f'{self.valor}'

class Tablero:
    def __init__(self, ladoMaximo:int):
        self.ladoMaximo = ladoMaximo
        self.tablero = []
        self.crear()
        self.distribuirNaufragos(4)

    def crear(self):
        self.tablero = [
            [Celda(columna, fila, '🌊') for columna in range(self.ladoMaximo)]
            for fila in range(self.ladoMaximo)
            ]

    def mostrar(self):
        numeros = "   " + " ".join(f"{columna:2d}" for columna in range(1, self.ladoMaximo + 1))
        print(numeros)

        for indice, fila in enumerate(self.tablero, start=1):
            mapa_fila = " ".join(str(celda) for celda in fila)
            print(f"{indice:2d} {mapa_fila}")

    def actualizarCelda(self, fila:int, columna:int, valor:str):
        self.tablero[fila - 1][columna - 1].valor = valor

    def hayNaufrago(self, fila:int, columna:int):
        return self.tablero[fila -1][columna-1].naufrago

    def distribuirNaufragos(self, cantidad:int):
        colocados = 0

        while colocados < cantidad:
            fila = random.randint(0, self.ladoMaximo - 1)
            columna = random.randint(0, self.ladoMaximo - 1)

            if not self.tablero[fila][columna].naufrago:
                self.tablero[fila][columna].naufrago = True
                self.tablero[fila][columna].valor = '🏝️ '
                colocados += 1

class Sonda:
    def __init__(self, columna, fila):
        self.columna = columna
        self.fila = fila

    def sondear(self, tablero: Tablero):
        if tablero.hayNaufrago(self.fila, self.columna):
            print('Rescataste un naufrago')
            tablero.tablero[self.fila - 1][self.columna - 1].naufrago = False

        for i in range(tablero.ladoMaximo):
            if tablero.tablero[self.fila - 1][i].naufrago:
                print('Hay un naufrago alrededor')
                return

        for i in range(tablero.ladoMaximo):
            if tablero.tablero[i][self.columna -1].naufrago:
                print('Hay un naufrago alrededor')
                return

    def activar(self,tablero: Tablero):
        self.sondear(tablero)
        tablero.actualizarCelda(self.fila, self.columna, '🚨')

    def __str__(self):
        return f'\nSonda 🚨 desplegada en {self.columna}, {self.fila}\n'
                

class Naufrago:
    pass

def naufrago(dificultad):            

    match dificultad:
        case 'facil':
            intentos = 10
            ladoMaximo = 6
        case 'intermedio':
            intentos = 15
            ladoMaximo = 8
        case 'dificil':
            intentos = 20
            ladoMaximo = 10

    encontro = False

    tablero = Tablero(ladoMaximo)


    while intentos > 0:
        tablero.mostrar()

        print(f"\nTenes {intentos} intentos.")

        while True:                                                         # Encontrar manera de no repetir

            try:
                columna = int(input("Ingrese su numero de columna: "))

                if columna < 1 or columna > ladoMaximo:
                    print(f"Fuera de mapa. Matriz de {ladoMaximo}x{ladoMaximo}")
                else:
                    break

            except ValueError:
                print("\nSolo valores numericos (numeros).\n")

        while True:                                                         # Encontrar manera de no repetir

            try:
                fila = int(input("Ingrese su numero de fila: "))

                if fila < 1 or fila > ladoMaximo:
                    print(f"Fuera de mapa. Matriz de {ladoMaximo}x{ladoMaximo}")
                else:
                    break

            except ValueError:
                print("\nSolo valores numericos (numeros).\n")

        sonda = Sonda(columna, fila)

        print(sonda)
        sonda.activar(tablero)

        if encontro == True:
            print("Encontraste al naufrago.")
            break
        else:
            intentos -= 1
            time.sleep(1)

while True:
    print("""
-----------------------
    NAUFRAGO!!!!1!
-----------------------

- Facil
- Intermedio
- Dificil

q. Salir
""")

    dificultad = str(input("Ingrese su dificultad: ")).lower()

    if dificultad == 'q':
        break
    if dificultad not in ('facil','intermedio','dificil'):
        print("\nIngrese una opcion valida.")
    else:

        naufrago(dificultad)
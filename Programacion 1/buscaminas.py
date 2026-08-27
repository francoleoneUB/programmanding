import random, time

lado_maximo = 14

class Celda:
    def __init__(self, columna: int, fila: int, valor: str, oculto: bool = True):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.oculto = oculto

    def __str__(self):
        return f'{self.valor}'

def validarNumero(mensaje) -> int:
    while True:
        try:
            numero = input(f"{mensaje}")
            numero = int(numero)

            if numero < 0 or numero >= lado_maximo:
                print("\nFuera del mapa")
                continue

            return numero

        except ValueError:
            print("\nIngrese un numero valido")
            time.sleep(.5)

def crearMapa() -> list:
    global columnas
    columnas = validarNumero("Ingrese cuantas columnas quiere")

    global filas
    filas = validarNumero("Ingrese cuantas filas quiere")

    mapa_Oculto = [[Celda(columna, fila, '#') for columna in range(columnas)]
    for fila in range(filas)]

    mapa_Visible = [[Celda(columna, fila, '⬜️') for columna in range(columnas)]
    for fila in range(filas)]

    return mapa_Visible

def mostrar(mapa):
    time.sleep(1)
    numeros = "   " + " ".join(f"{columna:2d}" for columna in range(1, columnas + 1))
    print(numeros)

    for indice, fila in enumerate(mapa, start=1):
        mapa_fila = " ".join(str(celda) for celda in fila)
        print(f"{indice:2d} {mapa_fila}")

mostrar(crearMapa())

import random, time

class Celda:
    def __init__(self, columna: int, fila: int, valor: str, oculto: bool = True):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.oculto = oculto

    def __str__(self):
        return f'{self.valor}'

def validarNumero(mensaje, maximo) -> int:
    while True:
        try:
            numero = input(f"{mensaje}")
            numero = int(numero)

            if numero < 0 or numero > maximo:
                print("\nFuera del mapa")
                continue

            return numero

        except ValueError:
            print("\nIngrese un numero valido")
            time.sleep(.5)

def crearMapa(dificultad) -> list:
    global columnas
    global filas
    global minas_Totales

    match dificultad:
            case 'facil':
                columnas = 9
                filas = 9
                minas_Totales = 14
            case 'intermedio':
                columnas = 16
                filas = 16
                minas_Totales = 40
            case 'dificil':
                columnas = 30
                filas = 16
                minas_Totales = 99

    global mapa_Oculto
    mapa_Oculto = [[Celda(columna, fila, '0') for columna in range(columnas)]
    for fila in range(filas)]

    global mapa_Visible
    mapa_Visible = [[Celda(columna, fila, '🟦') for columna in range(columnas)]
    for fila in range(filas)]

    colocados = 0

    while colocados < minas_Totales:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)

        if mapa_Oculto[columna][fila] == "M":
            continue
        else:
            mapa_Oculto[columna][fila].valor = "M"
            colocados += 1

def mostrar(mapa):
    time.sleep(1)
    numeros = "   " + " ".join(f"{columna:2d}" for columna in range(1, columnas + 1))
    print(numeros)

    for indice, fila in enumerate(mapa, start=1):
        mapa_fila = " ".join(str(celda) for celda in fila)
        print(f"{indice:2d} {mapa_fila}")

def descubrir_Celda(mapa_Oculto, mapa_Visible):
    posiciones = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    minasAlrededor = 0

    columna = validarNumero("Ingrese su columna: ", columnas) -1
    fila = validarNumero("Ingrese su fila: ", filas) -1 
    

    if mapa_Oculto[fila][columna].valor == "M":
        return False

    for deltaFila, deltaColumna in posiciones:
        filaAdyacente = fila + deltaFila
        columnaAdyacente = columna + deltaColumna

        if 0 <= filaAdyacente < filas and 0 <= columnaAdyacente < columnas:
            celda = mapa_Oculto[filaAdyacente][columnaAdyacente]

            if celda.valor == "M":
                minasAlrededor += 1

    mapa_Oculto[fila][columna].valor = f"{minasAlrededor}"
    mapa_Visible[fila][columna].valor = minasAlrededor

    return True

while True:
    print("""
-----------------------
    buscaminas!!!!1!
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

        crearMapa(dificultad)
        mostrar(mapa_Visible)

        while True:
            resultado = descubrir_Celda(mapa_Oculto, mapa_Visible)

            if resultado == False:
                break

            mostrar(mapa_Visible)

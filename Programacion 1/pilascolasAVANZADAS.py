import time

def primerEjercicio():
    print(f"Primer ejercicio: {[i**2 for i in range(1,11)]}")

primerEjercicio()

def segundoEjercicio():
    print(f"Segundo ejercicio: {[i for i in range(1,21) if i%2 == 0]}")

segundoEjercicio()

def tercerEjercicio(lista):
    print(f"Tercer ejercicio: {[i.capitalize() for i in lista]}")

tercerEjercicio(["Pepe","GAbriel","santhino", "ramiro"])

def cuartoEjercicio(lista):
    print(f"Cuarto ejercicio: {[i for i in lista if len(i)>4]}")

cuartoEjercicio(["Pepe","GAbriel","santhino", "ramiro"])

def quintoEjercicio(lista):
    print(f"Quinto ejercicio: {[i for i in lista if i < 0]}")

quintoEjercicio([5,3,7,-1,6,-7])

def sextoEjercicio(lista):
    print(f"Sexto ejercicio: {lista[:3]}")

sextoEjercicio([3,6,3,7,3])

def septimoEjercicio(lista):
    print(f"Septimo ejercicio: {lista[-2::]}")

septimoEjercicio([3,6,3,7,3])

def octavoEjercicio(lista):
    listaCopia = lista[:]
    print(f"Octavo ejercicio: Listo {listaCopia}")

octavoEjercicio([3,6,3,7,3])

def novenoEjercicio(lista):
    print(f"Decimo ejercicio: {lista[::-1]}")

novenoEjercicio([1,2,3,4,5,6,7,8,9,10])

def desafio():
    colectivos = [
        [60,143,36,True],
        [60,41,36,True],
        [60,97,38,False],
        [130,23,41,False],
                  ]

    def chequearNumero(placeholder:str):
        while True:
            numero = input(placeholder)

            try:
                return int(numero)
            except:
                print("\n \033[31mSolo se permiten valores numericos.\033[0m")
                time.sleep(0.5)

    def chequearSiONo(placeholder:str):
        while True:
            string = (input(placeholder)).lower()

            if isinstance(placeholder, str):
                if string == 'si':
                    return True
                elif string == 'no':
                    return False

    def agregarColectivo():
        numeroLinea    = chequearNumero("\nIngrese el numero de linea del colectivo: ")
        numeroInterno  = chequearNumero("\nIngrese el numero interno del colectivo: ")
        numeroAsientos = chequearNumero("\nIngrese el numero de asientos: ")
        accesibilidad  = chequearSiONo("\nEl colectivo es apto para discapacitados? (Si/No): ")

        colectivos.append([numeroLinea, numeroInterno, numeroAsientos, accesibilidad])

    def eliminarColectivo():
        numeroLinea    = chequearNumero("\nIngrese el numero de linea del colectivo: ")
        numeroInterno  = chequearNumero("\nIngrese el numero interno del colectivo: ")

        for i in colectivos:
            if i[0] == numeroLinea and i[1] == numeroInterno:
                colectivos.remove(i)
                print(f'\nListo! Colectivo {numeroInterno} de la linea {numeroLinea} eliminado.')
                time.sleep(1)
                return

        print('No se encontro un colectivo con esos numeros')

    def mostrarColectives():
        numeroLinea    = chequearNumero("\nIngrese el numero de linea del colectivo: ")

        for i in colectivos[:]:
            if i[0] == numeroLinea:
                print(i)

        time.sleep(1)

    def accesibilidadPorLinea():
        numeroLinea    = chequearNumero("\nIngrese el numero de linea del colectivo: ")
        total = 0

        for i in colectivos:
            if i[0] == numeroLinea and i[3] == True:
                total += 1

        print(f'\nHay un total de {total} colectivos pro-discapacidad')
        time.sleep(1)

    def asientosMas27():
        numeroLinea    = chequearNumero("\nIngrese el numero de linea del colectivo: ")
        total = 0

        for i in colectivos:
            if i[0] == numeroLinea and i[2] > 27:
                total += 1

        print(f'\nHay un total de {total} con mas de 27 asientos')
        time.sleep(1)

    while True:
        print("""
menu colectivero

1. Agregar colectivos
2. Eliminar colectivos por línea e interno*
3. Mostrar colectivos de una línea ordenados por ingreso
4. Informar cuántos colectivos aptos para personas con discapacidad hay por línea
5. Informar cuántos colectivos con más de 27 asientos hay por línea

q. Salir
""")

        eleccion = input("Ingrese su opcion: ")

        match eleccion:
            case "1":
                agregarColectivo()
            case "2":
                eliminarColectivo()
            case "3":
                mostrarColectives()
            case "4":
                accesibilidadPorLinea()
            case "5":
                asientosMas27()
            case "q":
                break
            case _:
                print("Ingrese una opcion valida")

desafio()
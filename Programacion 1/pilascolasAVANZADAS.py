# Generar una lista con los números del 1 al 10 elevados al cuadrado
# usando listas por comprensión y mostrarla por pantalla

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
    def chequearNumero(placeholder:str):
        while True:
            numero = input(placeholder)

            try:
                return int(numero)
            except:
                print("Ingrese una opcion valida")

    def chequearString(placeholder:str):
        while True:
            string = (input(placeholder)).lower()

            if isinstance(placeholder, str):
                return string

    def agregarColectivo():
        numeroLinea = chequearNumero("Ingrese el numero de linea del colectivo: ")
        numeroInterno = chequearNumero("Ingrese el numero interno del colectivo: ")
        numeroAsientos = chequearNumero("Ingrese el numero de asientos: ")
        accesibilidad = chequearString("El colectivo es apto para discapacitados? (Si/No): ")

    while True:
        print("""
menu colectivero

1. Agregar colectivos
2. Eliminar colectivos por línea e ingreso*
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
                #eliminarColectivo()
                pass
            case "3":
                #mostrarColectivos()
                pass
            case "4":
                #accesibilidadPorColectivo()
                pass
            case "5":
                #asientosMas27()
                pass
            case "q":
                break
            case _:
                print("Ingrese una opcion valida")

desafio()
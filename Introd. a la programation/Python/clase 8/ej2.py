import random

numero = random.randint(1000,9999)

while True:
    numeroIngresado = int(input("Ingrese un numero: "))

    try:
        if numeroIngresado == -1:
            print("\n Saliendo... \n")
            break

        if numeroIngresado < numero:
            print("El numero secreto es mayor\n")
        elif numeroIngresado > numero:
            print("El numero secreto es menor\n")
        else:
            print("\nGanaste!")
            break
    except:
        print("Ingrese un numero valido")
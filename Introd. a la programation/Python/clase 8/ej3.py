import random

numero = str(random.randint(1000,9999))
numero = tuple(numero)
print(numero)
l = 1

while True:
    numeroIngresado = input(f"Intento {l}: ")

    try:
        int(numeroIngresado)
    except:
        print("\n \033[31mIngrese un numero valido.\033[0m \n")

    if numeroIngresado == '-1':
        print("\n \033[90mSaliendo...\033[0m \n")
        break

    correcto = 0
    aproximado = 0

    for i in range(len(numeroIngresado)):
        if numeroIngresado[i] == numero[i]:
            correcto += 1
        elif numeroIngresado[i] in numero:
            aproximado += 1
    
    print(f"{correcto} digito/s correcto/s y {aproximado} digito/s aproximado/s")

    l += 1
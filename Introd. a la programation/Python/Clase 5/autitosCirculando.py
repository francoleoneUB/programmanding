contadorPar = 0
contadorImpar = 0

while True:
    terminacion = float(input("Ingrese un numero: "))
    
    if terminacion == -1:
        print(f"Pasaron {contadorPar} autos terminando en un numero par.\nPasaron {contadorImpar} autos terminando en un numero impar.")
        break

    if terminacion % 2 == 0:
        contadorPar += 1
    else:
        contadorImpar += 1


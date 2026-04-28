while True:
    numero = float(input("Ingrese un numero: "))

    if numero % 1 == 0 and numero > 0:
        break
    else:
        print("Ingrese un numero natural")

i = 0
resultado = 1

while i < numero:
    resultado = resultado * (numero - i)
    i += 1

print(resultado)
numero = str(input("Ingrese su numero entero: "))
letras = list(numero)

i = len(letras)

while True:
    if i == 0:
        break

    if i%3 == 0:
        letras.insert(-i,",")

    i -= 1

print("".join(letras))
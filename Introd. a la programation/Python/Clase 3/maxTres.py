numeros = []
i = 0

while i < 3:
    numeros.append(float(input("Ingrese el numero")))

    i += 1

print(f"El mayor es {max(numeros)}")
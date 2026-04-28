nombre = str(input("Ingrese el nombre a invertir: "))
nombreInvertido = []

i = 0

for i in range(len(nombre)):
    nombreInvertido.append(nombre[-(i+1)])

print("".join(nombreInvertido))
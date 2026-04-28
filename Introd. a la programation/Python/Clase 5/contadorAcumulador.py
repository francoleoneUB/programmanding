listaNumeros = []

while True:
    numero = float(input("Ingrese un numero: "))
    
    if numero == -1:
        print(f"El mayor es {max(listaNumeros)} y el menor es {min(listaNumeros)}")
        break
    
    if numero % 1 == 0 and numero > 0:
        listaNumeros.append(numero)
    else:
        print("Ingrese un numero entero y mayor a 0")
    
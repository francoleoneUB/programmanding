mayores = []
menores = []
edades = []

while True:
    edad = int(input("Ingrese su edad: "))

    if edad == -1:
        total = 0

        for i in range(len(edades)):
            total += edades[i]
        
        print(f"Hay {len(mayores)} personas mayores de edad, {len(menores)} personas menores de edad. El promedio de edades es {total/len(edades)}")
        break

    if edad < 0 and edad > 100:
        print("Ingrese una edad valida")
    elif edad < 18:
        menores.append(edad)
        edades.append(edad)
    else:
        mayores.append(edad)
        edades.append(edad)
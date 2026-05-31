temperaturas = [17, -3, 28, 11, 24, -1, 19, 26, 8, 14, 22, -5, 26, 10, -2, 21, 15, 29, 7, 13, 25, -4, 18, 12, 27, 9, 23, 16, 20, 6]
temperaturas.sort()

print(temperaturas)

def temperaturaMinima(listaTemperaturas):
    minTemp = listaTemperaturas[0]

    for i in listaTemperaturas:
        if minTemp > listaTemperaturas[i-1]:
            minTemp = listaTemperaturas[i-1]
    
    return minTemp

def temperaturaMaxima(listaTemperaturas):
    maxTemp = listaTemperaturas[0]

    for i in listaTemperaturas:
        if maxTemp < listaTemperaturas[i-1]:
            maxTemp = listaTemperaturas[i-1]
    
    return maxTemp

def temperaturaPromedio(listaTemperaturas):
    total = 0
    for i in listaTemperaturas:
        total += listaTemperaturas[i-1]
        return total / 30

def cuantasBajoCero(listaTemperaturas):
    cantidad = 0
    for i in listaTemperaturas:
        if listaTemperaturas[i-1] < 0:
            cantidad += 1
    
    return cantidad

print("""
Temperaturas Mensuales
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
      """)

for i in temperaturas:
    print(i)

print(f"""
Estadisticas
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
min: {temperaturaMinima(temperaturas)}
max: {temperaturaMaxima(temperaturas)}
mean: {temperaturaPromedio(temperaturas)}
Dias bajo cero: {cuantasBajoCero(temperaturas)}
""")
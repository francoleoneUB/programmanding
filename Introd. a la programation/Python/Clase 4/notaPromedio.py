cantidadAlumnos = int(input("Cantidad de alumnos: "))

i = 0
total = 0

while i < cantidadAlumnos:
    total += float(input("Nota de examenes: "))

    i += 1

print(f"Promedio de: {total/cantidadAlumnos}")
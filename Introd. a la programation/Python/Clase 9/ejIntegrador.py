def guardarAlumnos(nombre,nota):
    with open("Clase 9/archivo.txt","a",encoding="utf-8") as archivo:
        archivo.write(f'{nombre},{nota}\n')

def agregarDatos():
    nombre = str(input("Ingrese el nombre del contacto: "))
    nota = str(input("Ingrese el numero de nota: "))

    guardarAlumnos(nombre,nota)

notas = []

with open("Clase 9/archivo.txt","r",encoding="utf-8") as archivo:

        for line in archivo:
            line = line.strip()

            nombre, nota = line.split(",")

            notas.append(int(nota))

            print(f"{nombre},{nota}")

print(f'\nPromedio: {sum(notas) / len(notas)}')
print(f'Nota mas alta: {max(notas)}')
print(f'Nota mas baja: {min(notas)}')
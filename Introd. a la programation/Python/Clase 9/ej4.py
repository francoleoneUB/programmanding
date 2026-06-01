def guardarContacto(nombre,telefono):
    with open("Clase 9/archivo.txt","a",encoding="utf-8") as archivo:
        archivo.write(f'\n{nombre},{telefono}')

def agregarContacto():
    nombre = str(input("Ingrese el nombre del contacto: "))
    telefono = str(input("Ingrese el numero de telefono: \033[1;30m(+54)\033[0m "))

    guardarContacto(nombre,telefono)

with open("Clase 9/archivo.txt","r",encoding="utf-8") as archivo:

        for line in archivo:
            line = line.strip()

            nombre, telefono = line.split(",")

            print(f"Nombre: {nombre} - Teléfono: {telefono}")

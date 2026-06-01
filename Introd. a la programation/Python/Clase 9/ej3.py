with open("Clase 9/archivo.txt", "r", encoding="utf-8") as archivo:
    print(archivo.readline())

    print(archivo.read())

    archivo.seek(0)

    print(archivo.read())
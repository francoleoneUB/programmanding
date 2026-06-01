with open("Clase 9/archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

lineas = len(contenido.splitlines())
palabras = len(contenido.split())
caracteres = len(contenido)

print("Cantidad de lineas:", lineas)
print("Cantidad de palabras:", palabras)
print("Cantidad de caracteres:", caracteres)
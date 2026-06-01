alumnos = ['alumno A','alumno E','alumno I','alumno O','alumno U']

with open("Clase 9/archivo.txt","w",encoding="utf-8") as archivo:
    for i in range(len(alumnos)):
        print(i)
        contenido = archivo.write(f'{i+1} - {alumnos[i]}\n')
def escribirFrases():
    with open("Clase 9/archivo.txt","w",encoding="utf-8") as archivo:
    
        archivo.write(f"""Python es fácil
Me gusta python
JAVA y Python""")

escribirFrases()

total = 0

with open("Clase 9/archivo.txt","r",encoding="utf-8") as archivo:
    for line in archivo:
        if 'python' in line.lower():
            total += 1
        
    print(f'Se encontro {total} veces')
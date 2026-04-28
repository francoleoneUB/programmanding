multiplo = int(input("Ingrese el numero del que desea ver la tabla: "))

i = 1
total = 0

while i < 13:
    total += multiplo*i
    
    i+=1

print(f"La suma de los 12 numeros da: {total}")
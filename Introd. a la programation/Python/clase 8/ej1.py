import random

def bloqueando(n):
    lista = []

    try:
        lista = (random.sample(range(0,101),n))
    except ValueError:
        return "n tiene que ser menor a 100 \n"
    
    return lista

def eliminando(n):
    lista = []
    while True:
        for i in range(n+1):
            lista.append(random.randint(0,100))
        
        listaPurgada = set(lista)

        if len(listaPurgada) >= n:
            lista = list(listaPurgada)[:n]
            break
    
    return lista

n = int(input("Ingrese su n: "))

print(f"bloquenado: {bloqueando(n)}")
print(f"eliminando: {eliminando(n)}")
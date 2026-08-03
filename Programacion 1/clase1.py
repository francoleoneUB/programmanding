import random

def eliminarCoincidencias(primeraLongitud:int, segundaLongitud:int):
    primeraLista = []
    segundaLista = []
    resultado = []

    primeraLista = random.choices(range(0, 11), k = primeraLongitud)

    segundaLista = random.sample(range(0, segundaLongitud), k = segundaLongitud)

    for i in primeraLista:
        if i not in segundaLista:
            resultado.append(i)

    print("Lista original: ", primeraLista)
    print("Valores a eliminar: ", segundaLista)
    print("Resultado: ", resultado)

# eliminarCoincidencias(8,2)

def agregarValorManteniendoOrden(A, N):
    A = list(A)

    try: 
        A.index(N)
        print("N ya esta dentro de A")
    except ValueError:
        for i in range(len(A)):
            if A[i] > N:
                A.insert(i, N)
                break

        print(A)

# agregarValorManteniendoOrden([1,2,4,5,7,8], 3)

def ordenarLista(lista):

    # Cortesia de StackOverflow
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):

            if lista[i] > lista[j]:
               lista[i], lista[j] = lista[j], lista[i]

    return lista

def sumarListas(M, N):
    M = ordenarLista(list(M))
    N = ordenarLista(list(N))

    MN = M + N

    print(ordenarLista(MN))

# sumarListas([1,5,6,3],[2,4,8,7])

def listaAlumnos():
    lista = []

    while True:
        nombre = (str(input("\nNombre (fin para finalizar): ")))
        nombre = nombre.capitalize()

        if nombre == 'Fin':
            for i in range(len(lista)):
                print(f"{i+1:02d} {lista[i]}")
            break

        lista.append(nombre)
        print("\033[32mAlumno agregado correctamente.\033[0m")

# listaAlumnos()

def listaDeItems():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lista = []
    largoLista = random.randint(5, 10)
    for x in range(0, largoLista):
        lista.append(random.choice(alfabeto))
    return lista

def unionListas():
    lista = listaDeItems()
    liste = listaDeItems()

    listo = list(set(lista).intersection(liste))
    print(lista,liste,listo)

# unionListas()

def listaDeItemsModificado():
    lista = []
    largoLista = random.randint(1,20)
    for x in range(0, largoLista):
        lista.append(random.randint(0,9))
    return lista

def unionListasModificado():
    lista = listaDeItemsModificado()
    liste = listaDeItemsModificado()

    listo = list(set(lista).intersection(liste))
    print(lista,liste,listo)

# Para evitar que la tercera lista muestre duplicados se usa la funcion set(). O simplemente eliminar uno de los repetidos con count(), index() y pop().

# unionListasModificado()
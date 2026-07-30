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

def ordenarYSumarListas(M, N):
    M = ordenarLista(list(M))
    N = ordenarLista(list(N))

    MN = M + N

    print(ordenarLista(MN))

ordenarYSumarListas([1,5,6,3],[2,4,8,7])
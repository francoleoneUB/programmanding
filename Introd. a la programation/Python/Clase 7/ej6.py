def sonAnagramas(primerPalabra, segundaPalabra):
    primerPalabra = list(primerPalabra)
    segundaPalabra = list(segundaPalabra)

    primerPalabra.sort()
    segundaPalabra.sort()

    for i in range(len(primerPalabra)):
        if primerPalabra[i] != segundaPalabra[i]:
            return False
    
    return True

print(sonAnagramas('torpes','postre'))
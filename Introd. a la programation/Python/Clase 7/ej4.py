def appImportante(cadena):

    cadena = list(cadena)

    for i in range(len(cadena)):
        if cadena[i] in ("a","e","i","o","u"):
            cadena.insert(i,cadena[i].upper())
            cadena.pop(i+1)
    
    print(''.join(cadena))

appImportante(str(input("Ingrese su texto: ")))
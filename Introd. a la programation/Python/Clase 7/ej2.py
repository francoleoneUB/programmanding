def esPanvolica(cadena):
    contieneA = False
    contieneE = False
    contieneI = False
    contieneO = False
    contieneU = False

    for i in range(len(cadena)):
        if cadena[i] == "A":
            contieneA = True
        elif cadena[i] == "E":
            contieneE = True
        elif cadena[i] == "I":
            contieneI = True
        elif cadena[i] == "O":
            contieneO = True
        elif cadena[i] == "U":
            contieneU = True

    if contieneA and contieneE and contieneI and contieneO and contieneU:
        return "Es panvólica"
    else:
        return "No es panvólica"
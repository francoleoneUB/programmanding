def validar(password):
    password = list(password)

    cumpleLargo = False
    totalNumeros = 0
    contieneMayuscula = False
    contieneMinuscula = False

    if len(password) >= 8:
        cumpleLargo = True

    for i in range(len(password)):
        if password[i].isdigit():
            totalNumeros += 1
        elif password[i].isupper():
            contieneMayuscula = True
        elif password[i].islower():
            contieneMinuscula = True
    
    if totalNumeros >= 2 and contieneMayuscula and contieneMinuscula and cumpleLargo:
        print(True)
    else:
        print(False)

validar(str(input("Ingrese su clave: ")))
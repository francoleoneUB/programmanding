tipo = str(input("Tipo de tarjeta: "))

match tipo:
    case '1':
        print(f"Su limite aumentara un 25%")
    case '2':
        print(f"Su limite aumentara un 35%")
    case '3':
        print(f"Su limite aumentara un 40%")
    case _:
        print(f"Su limite aumentara un 50%")
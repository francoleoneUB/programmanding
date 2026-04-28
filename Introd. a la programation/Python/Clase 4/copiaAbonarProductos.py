
while True:
    precio = float(input("Precio: $"))
    
    if precio == 0:
        print("Saliendo..")
        break

    paga = float(input("Abona con: $"))

    diferencia = precio - paga

    if diferencia > 0:
        print(f"Le faltan: ${diferencia} pesos.")
    elif diferencia == 0:
        print("Pago con lo justo")
    else:
        print(f"Su vuelto es: ${diferencia*-1} pesos.")
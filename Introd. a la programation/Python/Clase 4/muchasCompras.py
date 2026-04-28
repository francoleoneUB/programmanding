total = 0

while True:
    precio = float(input("Ingrese el precio: $"))

    if precio == 0:
        print("Saliendo..")
        break
    
    total += precio

paga = float(input("Ingrese lo que desea abonar: $"))

diferencia = total - paga

if diferencia > 0:
    print(f"Le faltan: ${diferencia} pesos.")
elif diferencia == 0:
    print("Pago con lo justo")
else:
    print(f"Su vuelto es: ${diferencia*-1} pesos.")
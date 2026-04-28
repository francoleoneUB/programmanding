cantidadBoletos = int(input("Cantidad de boletos: "))
precioBoleto = 67000    # sixseven

if cantidadBoletos >= 5:
    print("No se pueden comprar mas de 4 boletos por persona")
else:
    print(f"Total: {cantidadBoletos*precioBoleto}")
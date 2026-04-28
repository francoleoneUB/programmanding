meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
eleccion = int(input("Ingrese el mes que desea ver: "))

if eleccion > 0 and eleccion <= 12:
    print(meses[eleccion-1])
else:
    print("Ingrese un valor entre 1 y 12.")
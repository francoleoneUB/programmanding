salario = int(input("Ingrese su salario mensual: "))
tasaAhorro = float(input("Ingrese cuanto ahorra al mes: "))
precio = float(input("Ingrese el precio del producto: "))

print(f"Tardaria {precio/(salario*tasaAhorro)} meses en comprarlo")
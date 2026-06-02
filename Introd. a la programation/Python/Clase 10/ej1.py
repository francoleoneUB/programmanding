class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

class Rectangulo:
    def __init__(self,base = 1,altura = 1):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        print(f"Area: {self.base*self.altura} u²")
    
    def calcularPerimetro(self):
        print(f"Perimetro: {(self.base + self.altura)*2} u")

class Estudiante:
    def __init__(self,nombre,notas):
        self.nombre = str(nombre)
        self.notas = notas
    
    def promedio(self):
        print(f"Promedio: {sum(self.notas)/len(self.notas)}")
    
    def promedioAprobado(self):
        if self.promedio() >= 6:
            return True

class CuentaMacro:
    def __init__(self,titular,saldo):
        self.titutlar = titular
        self.saldo = saldo
    
    def depositar(self,monto):
        self.saldo += monto
    
    def retirar(self,monto):
        if self.saldo > monto:
            self.saldo -= monto
        else:
            print("No tiene suficiente dinero.")

class Ventilador:
    def __init__(self,estado,velocidad):
        estado = False
        self.estado = estado
        self.velocidad = velocidad
    
    def alterarEstado(self):
        if self.estado == False:
            self.estado = True
            self.velocidad = 1
        else:
            self.estado = False
            self.velocidad = 0
    
    def aumentarVelocidad(self):
        self.velocidad += 1

        if self.velocidad == 4:
            self.velocidad = 0

class Libro:
    def __init__(self,titulo,autor,prestado):
        self.titulo = titulo
        self.autor = autor
        self.prestado = prestado
    
    def prestar(self):
        if self.prestado == True:
            print("El libro ya esta prestado")
        else:
            self.prestado == True
    
    def devolver(self):
        if self.prestado == False:
            print("El libro ya esta en el catologo")
        else:
            self.prestado == False

class Celular:
    def __init__(self,marca,modelo,bateria):
        self.marca = marca
        self.modelo = modelo
        if bateria > 0 and bateria < 100:
            self.bateria = bateria
        else:
            print("Ingrese un porcentaje de bateria valido.")
    
    def hacerLlamada(self,duracion):
        if duracion > 0:
            self.duracion = duracion

            self.bateria -= duracion
        else:
            print("Ingrese una duracion valida.")
    
    def cargar(self):
        self.bateria = 100

class Calculadora:
    def sumar(a,b):
        return a + b
    
    def restar(a,b):
        return a - b

    def multiplicar(a,b):
        return a * b
    
    def dividir(a,b):
        return a/b

calculadora = Calculadora()
calculadora.sumar(3,3) # ERROR -------------------------

class Auto:
    def __init__(self,marca,modelo,kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje
    
    def conducir(self,distancia):
        self.kilometraje += distancia
    
    def mostrarInformacion(self):
        print(f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Kilometraje: {self.kilometraje}
        """)

class CarritoCompras:
    def __init__(self,productos):
        self.productos = productos
    
    def agregarProductos(self,producto):
        productos = self.productos
        productos.append(producto)
    
    def mostrar(self):
        print(self.productos)

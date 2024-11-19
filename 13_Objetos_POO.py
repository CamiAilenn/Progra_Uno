'''#Ejercicio 1: Clase simple 
#Crear una clase Persona que tenga las características nombre y edad.  La persona debe poder 
#mostrar un mensaje saludando presentándose con su nombre y edad.  Se debe crear la clase e 
#implementarla. 
class Persona:
    def __init__(self, nombre, edad)-> None:
        self.nombre:str = nombre
        self.edad:int = edad
    
    def saludo(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años!!!")

persona_uno = Persona("Camila F", 31)
persona_uno.saludo()


#Ejercicio 2: Clase para representar un Libro 
#Crear una clase Libro que tenga las características títuto, autor y año de publicación.  Del libro se 
#debe poder obtener información, mostrando por mensaje todos sus datos.  Se debe crear la clase 
#e implementarla.
class Libro:
    def __init__(self, titulo, autor, año_publicado)->None:
        self.titulo = titulo
        self.autor = autor
        self.año_publicado:int = año_publicado
    
    def mostrar_informacion(self):
        print(f"""El libro llamado {self.titulo} fue escrito por {self.autor} fue publicado en el año {self.año_publicado} """)
    

libro_uno = Libro("Sol de medianoche", "Stephenie Meyer", 2020)
libro_uno.mostrar_informacion()

#Ejercicio 3: Clase para representar un Rectángulo 
#Crear una clase rectángulo que tenga las características base y altura.  Del rectángulo se debe 
#poder calcular el área y el perímetro.  Se debe crear la clase e implementarla. 
class Rectangulo():
    def __init__ (self, base, altura)->None:
        self.base:int = base
        self.altura:int = altura
    
    def calcular_perimetro(self):
        perimetro = 2 * self.base + 2 * self.altura
        print(f"El perimetro de un rectangulo de base {self.base} y altura {self.altura} es {perimetro}")
    def calcular_area(self):
        area = self.base * self.altura
        print(f"El area de un rectangulo de base {self.base} y altura {self.altura} es {area}")

base_rectangulo = int(input("¿Cual es la base del rectangulo? "))
altura_rectangulo = int(input("¿Cual es la altura del rectangulo? "))
rectangulo_uno = Rectangulo(base_rectangulo, altura_rectangulo)
rectangulo_uno.calcular_area()
rectangulo_uno.calcular_perimetro()

#Ejercicio 4: Clase para representar una Calculadora 
#Crear una clase Calculadora que pueda calcular suma, resta, multiplicación y división.  Se debe 
#crear la clase e implementarla. 

class Calculadora():
    def __init__ (self, numero_uno, numero_dos)-> None:
        self.numero_uno = numero_uno
        self.numero_dos = numero_dos
    
    def sumar(self):
        suma = self.numero_uno + self.numero_dos
        print(f"La suma entre {self.numero_uno} y {self.numero_dos} es {suma}")
    def restar(self):
        resta = self.numero_uno - self.numero_dos
        print(f"La resta entre {self.numero_uno} y {self.numero_dos} es {resta}")
    def mutiplicar(self):
        multiplicacion = self.numero_uno * self.numero_dos
        print(f"La multiplicacion entre {self.numero_uno} y {self.numero_dos} es {multiplicacion}")
    def dividir(self):
        if self.numero_dos == 0:
            print(f"No se puede realizar la division porque el divisor es cero")
        else:
            division = self.numero_uno / self.numero_dos
            print(f"La division entre {self.numero_uno} y {self.numero_dos} es {division}")

numero_ingresado_uno = int(input("Ingrese el primer numero: "))
numero_ingresado_dos = int(input("Ingrese el segundo numero: "))
calculator = Calculadora(numero_ingresado_uno,numero_ingresado_dos)
calculator.sumar()
calculator.restar()
calculator.mutiplicar()
calculator.dividir()

#Ejercicio 5: Herencia de clases 
#Crear una clase Animal que tenga la característica nombre.  La clase Perro que herede de Animal 
#las características y realice el sonido “guau guau”.  La clase Gato que herede de Animal las 
#características y realice el sonido “Miau”.  Del gato y el perro se debe poder mostrar el sonido que 
#realizan.  Se debe crear la clase e implementarla.

class Animal:
    def __init__(self, nombre)->None:
        self.nombre = nombre
    def mostrar_nombre(self):
        print(f"El nombre de su mascota es: {self.nombre}")

class Perro(Animal):
    def __init__(self, nombre)->None:
        super().__init__(nombre)
        self.sonido = "Guau Guau"
    def presentacion(self):
        print(f"El animal {self.nombre} es un perro y hace {self.sonido}")

class Gato(Animal):
    def __init__(self, nombre)->None:
        super().__init__(nombre)
        self.sonido = "Miaaaau"
    def presentacion(self):
        print(f"El animal {self.nombre} es un gato y hace {self.sonido}")

animal_uno = Perro("Serena")
animal_uno.mostrar_nombre()
animal_uno.presentacion()

animal_dos = Gato("Pelusa")
animal_dos.mostrar_nombre()
animal_dos.presentacion()

'''
#Ejercicio 6: Encapsulamiento 
#Crear una clase Cuenta Bancaria que tenga las características titular y saldo encapsulado.  De la 
#cuenta bancaria se puede obtener el saldo, depositar o retirar (en cada caso imprimir que fue 
#exitoso).  Se debe crear la clase e implementarla.

class CuentaBancaria():
    def __init__(self, titular, saldo)->None:
        self.__titular = titular
        self.__saldo:int = saldo
    
    def mostrar_saldo(self):
        print(f"El saldo de su cuenta es: {self.__saldo}")
    def ver_saldo(self):
        return self.__saldo
    
    def depositar(self,dinero_ingresado):
        self.__saldo += dinero_ingresado
        print("Operacion exitosa")
            
    def retirar(self):
        dinero_a_retirar = int(input("¿Cuanto dinero desea retirar? "))
        if dinero_a_retirar <= self.__saldo:
            self.__saldo -= dinero_a_retirar
            print("Operacion exitosa")
        else:
            print("Usted no puede retirar ese monto")
           

cuenta_cliente = CuentaBancaria("Camila F", 15) #Porque no sirve si paso los parametros como variables???
cuenta_cliente.mostrar_saldo()
print(cuenta_cliente.ver_saldo())

dinero_ingresado = int(input("¿Cuanto dinero desea ingresar? "))
cuenta_cliente.depositar(dinero_ingresado)

cuenta_cliente.mostrar_saldo()
print(cuenta_cliente.ver_saldo())



cuenta_cliente.retirar()

cuenta_cliente.mostrar_saldo()
print(cuenta_cliente.ver_saldo())

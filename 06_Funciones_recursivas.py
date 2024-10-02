#1. Realizar una función recursiva que calcule la suma de los primeros 
#números naturales:
def suma_naturales(numero: int)->int:
    '''Calculara la suma de los numeros naturales hasta el numero ingresado'''
    while numero < 0:
        numero = int(input("ERROR. Ingrese un numero natural (entero mayor a cero)"))
    
    if numero == 0:
        return 0
    else:
        return numero + suma_naturales(numero - 1)

numero = int(input("Ingrese un numero natural (entero mayor a cero)"))
resultado = suma_naturales(numero)
print("La suma de los numeros naturales hasta el" ,numero, "es", resultado) 

#Si ingreso mal el numero, me lo valida en la funcion pero en el print 
# de respuesta, por fuera de la funcion me imprime el original que puse
#Ademasno puedo validar haber ingresado el 0


#2. Realizar una función recursiva que calcule la potencia de un número:

def potencia (base:int,exponente:int)->int:
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)
print("La base es", base,"y el exponente es", exponente, "el resultado es:", resultado)


#3. Realizar una función recursiva que permita realizar la suma de los 
#dígitos de un número:

def sumar_digitos(numero:int)->int:
    """Va a sumar los digitos del numero introducido"""
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumar_digitos(numero // 10)
    #Con el modulo obtenemos la unidad del numero que sera sumada. 
    # Llamamos nuevamente a la funcion, pero al hacer la division entera
    # desestimamos la unidad, por lo que comienza de nuevo el ciclo.
numero = int(input("Ingrese un numero "))
resultado = sumar_digitos(numero)
print(resultado)


#Opcion 2
def sumar_digitos(numero:str, digitos:int, suma=0):
    digitos -= 1
    suma +=(numero[digitos])
    if digitos == 0:
        return suma
    else:
        return sumar_digitos(numero, digitos, suma)
numero = str(input("Ingrese un numero"))
digitos = len(numero)
print("La suma de los digitos es: ",sumar_digitos(numero, digitos))

#4.Realizar una función para calcular el número de Fibonacci de un número
#ingresado por consola. La función deberá seguir el siguiente prototipo
#En donde: número: el número ingresado por el usuario mediante consola, 
#utilizando nuestra función 
#get_int(mensaje,mensaje_error,mínimo,máximo,reintentos


#4.Realizar una función para calcular el número de Fibonacci de un número
#ingresado por consola

def fibonacci (num):
    '''Calculara el numero que se encuentra en la posicion indicada'''
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num(num - 1) + fibonacci(num - 2)

numero = int(input("Ingrese un numero "))
resultado = fibonacci(numero)
print(resultado)


#Numero primos son:
#● Número entero positivo mayor que el número uno y que 
#● solo puede ser divisible sin resto por el número uno y por el mismo.
#● Los primeros números primos son: 
#2,3,5,7,11,13,17,19,23,29,31,37,41,43,47, ...
#● Realizar un programa que solicite un número y a través de una función 
#recursiva determine si el número es primo

def numero_primo(numero:int,i=2):
    primo = numero % i
    if i == numero:
        return True
    elif primo == 0:
        return False
    else:
        return numero_primo(numero,i+1)

num = int(input("Ingrese un numero (mayor a 1): "))
if numero_primo(num):
    print("Es primo")
else:
    print("No es primo")
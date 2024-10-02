#Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
#como parámetro.

def mostrar_numero ():
    '''Mostrara el numero que ingrese'''
    numero = int(input("Ingrese un numero: "))
    print("El numero ingresado es: ", numero)
mostrar_numero()

#https://onlinegdb.com/NGmLWbxx4

def mostrar_numero (numero:int):
    '''Mostrara el numero que ingrese'''
    print("El numero ingresado es: ", numero)

mostrar_numero(12)

#https://onlinegdb.com/Jz6bfek3K

#Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.

def pedir_numero ()->int:
    '''Mostrara el numero que ingrese'''
    numero = int(input("Ingrese un numero: "))
    return numero

pedir_numero()

#https://onlinegdb.com/Gc_pSas5m


#Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La
#función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
#programa principal realizando la invocación o llamada.

def numero_par(numero:int)->bool:
    "Determina si el numero ingresado por usuario es par o no"
    par = numero % 2
    if par == 0:
        numero_par = True
    else:
        numero_par = False
    return numero_par


numero_usuario = int(input("Ingrese un numero: "))
if numero_par(numero_usuario):
    print("El numero es par")
else:
    print("El numero es impar")

#https://onlinegdb.com/KtV-GqTdtX

#Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en
#un rango determinado pasado por parámetro “desde”-“hasta”.

def validar_numero (numero:int, desde:int , hasta:int):
    '''Mostrara el numero que ingrese si esta entre los parametros "desde-hasta"
    Sino, lo volvera a pedir'''
    while numero < desde or numero > hasta:
        numero = int(input("Ingreso, no valido. Ingrese un numero: "))
    return numero
numero = int(input("Ingrese un numero: "))
inicio = int(input("Confirme el inicio del rango validacion del numero "))
fin = int(input("Confirme el final del rango validacion del numero "))

resultado = validar_numero(numero,inicio,fin)
print("El numero", resultado, "esta validado") 
#Puedo printiar en la funcion, pero no en el retorno


#https://onlinegdb.com/8PHfhT3pH


#Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la
#función Restar en sus 4 combinaciones.
# Restar1(int, int)->int:
def restar_uno(num_uno:int , num_dos:int)->int:
    """Diferencia entre dos numeros enteros por parametro, con un retorno entero"""
    diferencia = num_uno - num_dos
    return diferencia

numero_a = int(input("Ingrese un numero: "))
numero_b = int(input("Ingrese un numero: "))
print(restar_uno(numero_a,numero_b))
    
# Restar2()->int:
def restar_dos()->int:
    """Diferencia entre dos numeros enteros, con un retorno entero"""
    num_uno = int(input("Ingrese un numero: "))
    num_dos = int(input("Ingrese un numero: "))
    diferencia = num_uno - num_dos
    return diferencia
print(restar_dos())

# Restar3(int, int):
def restar_tres(num_uno:int , num_dos:int):
    """Diferencia entre dos numeros enteros por parametro, sin retorno"""
    diferencia = num_uno - num_dos
    print("La diferencia entre",num_uno,"y", num_dos, "es", diferencia)

numero_a = int(input("Ingrese un numero: "))
numero_b = int(input("Ingrese un numero: "))

restar_tres(numero_a,numero_b)


# Restar4():
def restar_cuatro():
    """Diferencia entre dos numeros enteros, sin retorno"""
    num_uno = int(input("Ingrese un numero: "))
    num_dos = int(input("Ingrese un numero: "))
    diferencia = num_uno - num_dos

restar_cuatro()

#https://onlinegdb.com/RFVhlhTqC

#Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
#solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
#dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
#por pantalla. Atención: pueden reutilizarse funciones ya creadas.

def realizarDescuento(numero):
    '''Validara el numero que ingrese este entre 10 y 100 
    calculara un descuento del 5% y mostrara el numero por pantalla
    Sino, lo volvera a pedir'''
    desde = 10
    hasta = 100
    while numero < desde or numero > hasta:
        numero = int(input("Ingreso, no valido. Ingrese un numero: "))
    descuento = numero - numero * 0.05
    return descuento

numero1 = int(input("Ingrese un numero: "))

realizarDescuento(numero1)
print ("El numero", numero1, "con un 5% de descuento es", realizarDescuento(numero1))

#https://onlinegdb.com/W1anxUL5D


#Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2
#los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
#variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice 
#la operación de dichos valores a través de una función. Mostrar el resultado por
#pantalla.

def sumar_restar(numero1:int, numero2:int, operacion:str)->int:
    '''Validara que los numeros ingresados esten entre 10 y 100 
    calculara luego la suma o resta de ambos, segun ingreso del usuario
    Retornara el resultado de la operacion'''
    if operacion == "s":
        retorno = numero1 + numero2
    else:
        retorno = numero1 - numero2     
    return retorno   

#Importar funciones de validacion
num_uno = int(input("Ingrese un numero: "))
while num_uno < 10 or num_uno > 100:
       num_uno = int(input("Ingreso, no valido. Ingrese un numero: "))
num_dos = int(input("Ingrese otro numero: "))
while num_dos < 10 or num_dos > 100:
       num_dos = int(input("Ingreso, no valido. Ingrese un numero: "))
operacion = input("Usted desea sumar (s) o restar (r): ").lower()
while operacion != "s" and operacion != "r":
    operacion = input("Ingreso no valido Usted desea sumar (s) o restar (r): ").lower()
resultado = sumar_restar(num_uno, num_dos, operacion)
print(resultado)


#https://onlinegdb.com/ihKmrksYN

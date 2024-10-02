#1. Mostrar los números ascendentes desde el 1 al 10
for i in range (10):
    print (i+1)

for i in range (1, 11):
    print (i)

#https://onlinegdb.com/YQGzOM0Tv

#2. Mostrar los números descendentes desde el 10 al 1
num = 10
for i in range (num):
    print(num - i)

#Opcion 2
for i in range(10,0,-1):
    print(i)

#https://onlinegdb.com/9y6P2HKz7
#https://onlinegdb.com/T42-UQUNNQ

#3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
num = int(input("Ingrese un numero: "))
for i in range (num+1):
    print(i)
#https://onlinegdb.com/KBEiaO8fW

#4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
#ejemplo si se ingresa el numero 5:
#5 x 0 = 0
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15 …

num = int(input("Ingrese un numero: "))

for i in range(21):
    print(num, "x", i , "=", num * i)

#https://onlinegdb.com/BpKMQFmqv

#5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
# Mostrar la suma y el promedio de todos los números.
acumulador = 0
contador = 0
promedio = 0
num = 1
print("Usted ingresara 10 numeros, distintos de 0, si ingresa 0 interrumpira el ingreso")
while contador < 10 and num != 0:
        num = int(input("Ingrese un numero:"))
        acumulador += num
        if num != 0:
            contador += 1

       
promedio = acumulador / contador
print("La suma de todos los numeros ingresados es", acumulador, '\n'
      "Y el promedio de los numeros ingresados", promedio )
#https://onlinegdb.com/1dO9biW30

# CON FOR
acumulador = 0
contador = 0
for i in range (1,11):
    numero = int(input("Ingreseun numero: "))
    if numero == 0:
        break
    else:
        acumulador += numero
        contador += 1
promedio = acumulador / contador
print("La suma de todos los numeros ingresados es", acumulador, '\n'
      "Y el promedio de los numeros ingresados", promedio )

#6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
num = 3

for i in range (1,11):
    resto_cero_multiplos = i % num
    if resto_cero_multiplos == 0:
        print(i)
#https://onlinegdb.com/LS0m2dk8m

#7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)

for i in range (1,51):
    numeros_pares = i % 2
    if numeros_pares == 0:
        print(i)
#https://onlinegdb.com/flNX2CS09


#8. Realizar un programa que permita mostrar una pirámide de números. 

num = int(input("Ingrese un numero: "))
acumulador = "1"

for i in range (2,num+2):
    print(acumulador)
    i = str(i)
    acumulador += i

#https://onlinegdb.com/aWqG0QckH


#9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
#el número ingresado. Mostrar la cantidad de divisores encontrados.
num = int(input("Ingresa un numero: "))
contador = 0
for i in range (1,num+1):
    divisores = num % i
    if divisores == 0:
        contador += 1
        print(i, "Es un divisor de", num)
print(num, "tiene un total de", contador , "divisores")

#https://onlinegdb.com/YXfHgZeLWp

#10.Ingresar un número. Determinar si el número es primo o no.

num = int(input("Ingrese un numero: "))
num_primo = True
for i in range(2,num): #Inicio en 2 porque 1 es divisor de todos, y termino uno antes a si mismo
    primo = num % i
    if primo == 0:
        num_primo = False
if num_primo == True:
    if num <= 1:
        print("No es un numero valido")
    else:
        print ("Este numero es primo")
else: 
    print("Este numero NO es primo")

#https://onlinegdb.com/km24k4l9l
#https://onlinegdb.com/kQwmheg-C

#11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
#número ingresado. Informar cuántos números primos se encontraron

contador = 0
num = int(input("Ingrese un numero (mayor a 1): "))
while num <= 1:
    num = int(input("No valido. Ingrese un numero (mayor a 1): "))
    
for dividendo in range(2,num+1): #Inicio en 2 porque 1 es divisor de todos, y 
    num_primo = True
    for divisor in range (2,dividendo):
        primo = dividendo % divisor   # i modulo j, si el resto es cero, entonces i tiene divisores
        if primo == 0:
            num_primo = False
    if num_primo:
        print(dividendo, "es primo")
        contador += 1
print ("Hay", contador, "numeros primos")

#https://onlinegdb.com/m-9BtlODcu

# TODOS SIN EL 8 Y 11
#https://onlinegdb.com/uqae69xwB
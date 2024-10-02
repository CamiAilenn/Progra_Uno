#Ejercicio 1:
#Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su 
#sueldo para esa persona.
nombre = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo: $"))
aumento_sueldo = sueldo * 1.1

print(nombre, "su sueldo es $", aumento_sueldo)

#https://onlinegdb.com/veBQ1KxiI

#Ejercicio 2:
#Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), 
#adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad = int(input("¿Cual es su edad? "))
if edad < 0 or edad > 120:
    print("edad no valida")
elif edad <= 13:
    print("Usted es niño")
elif edad <= 17:
    print("Usted es adolescente")
elif edad > 18:
    print("Usted es mayor de edad")

#https://onlinegdb.com/c2k6cRYjE

#Ejercicio 3:
#Ingresar 5 números enteros, distintos de cero.
#Informar:
#a. Cantidad de pares e impares.
#b. El menor número ingresado.
#c. De los pares el mayor número ingresado.
#d. Suma de los positivos.
#e. Producto de los negativos.
numero = 0
contador = 0
acumulador_par = 0
acumulador_impar = 0
numero_menor = 10000000000000000
numero_mayor = -10000000000000000
numero_par_mayor = 0
acumulador_positivos = 0
acumulador_producto_negativos = 1

while contador < 5:
    
    numero = int(input("Ingrese un numero entero distinto de 0: "))
    numero_par = numero % 2
    #Ejercicio A   usar banderasssssssssssssssssssssss
    if numero_par == 0:
        acumulador_par += 1 
       # if numero_par = True
    else:
        acumulador_impar += 1
    #Ejercicio B    
    if numero < numero_menor:
        numero_menor = numero
    #Ejercicio C
    if numero > numero_mayor:
        numero_mayor = numero
        if numero_par == 0:
            numero_par_mayor = numero
    #Ejercicio D
    if numero > 0:
        acumulador_positivos += numero
    #Ejercicio E
    else:
        acumulador_producto_negativos *= numero
    contador += 1

#Ejercicio A
print(acumulador_par,"numeros pares ingresados.")
print(acumulador_impar,"numeros impares ingresados.")
#Ejercicio B
print(numero_menor,"fue el menor numero igresado")
#Ejercicio C
print(numero_par_mayor, "es el numero par mayor")
#Ejercicio D
print(acumulador_positivos, "Es la suma acumulada de los numeros positivos ingresados")
#Ejercicio E
print(acumulador_producto_negativos, "Es el producto de los numeros negativos ingresados")

#https://onlinegdb.com/8qMhKL3if
    

#Ejercicio 4:
#Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado 
#civil distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO ser soltero.'
edad = int(input("¿Cual es su edad? "))
estado_civil = input("¿Cual es su estado civil ")
if edad < 18 and estado_civil != "Soltero":
    print("Es muy pequeño para NO ser soltero")

#https://onlinegdb.com/g5evqRIeP


#Ejercicio 5:
#Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 
#por cada estadía como base, se pide el ingreso de una estación del año
#(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del Plata/Córdoba)
#para vacacionar para poder calcular el precio final: 
# en Invierno: 
# Bariloche tiene un aumento del 20%, 
# Cataratas y Córdoba tiene un descuento del 10% 
# Mar del Plata tiene un descuento del 20% 
# en Verano: 
# Bariloche tiene un descuento del 20% 
# Cataratas y Córdoba tiene un aumento del 10% 
# Mar del Plata tiene un aumento del 20% 
# en Otoño y Primavera: 
# Bariloche tiene un aumento del 10% 
# Cataratas tiene un aumento del 10% 
# Mar del Plata tiene un aumento del 10% 
# Córdoba tiene el precio sin descuento.

costo_base = 15000
costo_final = 0
aumento_diez = 1.1
aumento_veinte = 1.2
descuento_diez = 0.9
descuento_veinte = 0.8

estacion_año = input("Ingrese estacion del año: (Invierno - Verano - Otoño - Primavera) ").capitalize()
while estacion_año != "Invierno" and estacion_año != "Verano" and estacion_año != "Otoño" and estacion_año != "Primavera":
    estacion_año = input("No valido. Ingrese estacion del año: (Invierno - Verano - Otoño - Primavera) ").capitalize()
localidad = input("Indique destino (Bariloche - Cataratas - Mardelplata - Cordoba) ").capitalize()
while localidad != "Bariloche" and localidad != "Cataratas" and localidad != "Mardelplata" and localidad != "Cordoba":
    localidad = localidad = input("Indique destino (Bariloche - Cataratas - Mardelplata - Cordoba) ").capitalize()

if estacion_año == "Invierno":
    if localidad == "Bariloche":
        costo_final = costo_base * aumento_veinte
    elif localidad == "Mardelplata":
        costo_final = costo_base * descuento_veinte
    else:
        costo_final = costo_base * descuento_diez
elif estacion_año == "Verano":
    if localidad == "Bariloche":
        costo_final = costo_base * descuento_veinte
    elif localidad == "Mardelplata":
        costo_final = costo_base * aumento_veinte
    else:
        costo_final = costo_base * aumento_diez
else:
    if localidad == "Cordoba":
        costo_final = costo_base 
    else:
        costo_final = costo_base * aumento_diez


print("Usted ira a" , localidad , '\n'
      "Durante el", estacion_año , '\n'
      "El costo de su viaje sera: $", costo_final)

#https://onlinegdb.com/YukGrIsoI
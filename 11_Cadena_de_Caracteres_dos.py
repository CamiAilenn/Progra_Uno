#1) Crear una función que reciba como parámetro una cadena y determine la
#cantidad de vocales que hay de cada una (individualmente). La función
#retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
#la cantidad.
#Por ej:
#cadena = “murcielaguito”
#“a” 1
#“e” 1
#“i” 2
#“o” 1
#“u” 2

def contar_vocales(cadena:str)->list:
    """Ingresa una cadena, y cuenta las vocales que tiene"""
    vocales = []
    cadena.lower()
    acumulador_a = 0
    acumulador_e = 0
    acumulador_i = 0
    acumulador_o = 0
    acumulador_u = 0
    for i in cadena:
        if i == "a":
            acumulador_a += 1
        if i == "e":
            acumulador_e += 1
        if i == "i":
            acumulador_i += 1
        if i == "o":
            acumulador_o += 1
        if i == "u":
            acumulador_u += 1
    vocales =[["a", acumulador_a],
              ["e", acumulador_e],
              ["i", acumulador_i],
              ["o", acumulador_o],
              ["u", acumulador_u]]
    
    return vocales

"""cadena = "Hola como estas vos aaaa eee i ooo"
resultado = contar_vocales(cadena)
for i in range (len(resultado)):
    print(resultado[i])"""

#2) Crear una función que reciba una cadena y un caracter. La función deberá
#devolver el índice en el que se encuentre la primera incidencia de dicho
#caracter, o -1 en caso de que no esté.
def buscar_caracter(cadena:str, caracter:str)->int:
    """Ingresa una cadena y un caracter por parametro.
    Busca el caracter en la cadena. Si lo encuentra retorna la primera ubicacion.
    Si no lo encuentra devuelve -1"""

    for i in range(len(cadena)):
        if caracter == cadena[i]:
            resultado = i
            break
        else:
            resultado = -1
    return resultado

"""cadena ="Estamos probado"
print(buscar_caracter(cadena, "y"))"""


#3) Crear una función que reciba como parámetro una cadena y determine si la
#misma es o no un palíndromo. Deberá retornar un valor booleano indicando
#lo sucedido.
def invertir_cadena(cadena:str)->str:
    """Ingresa una cadena y la funcion invierte el orden de los caracteres"""
    nueva_cadena = ""
    for i in range(len(cadena)):
        caracter = cadena[len(cadena)-1-i]
        nueva_cadena += caracter
    return nueva_cadena

def polindromo (cadena:str)-> bool:
    """Ingresa una cadena por parametro.
    usa la funcion invertir cadena para darla vuelta
    Si es un polindromo retorna VERDADERO, sino FALSO.
    Polindromo: Palabra o frase que se lee igual de izquierda a derecha 
    que de derecha a izquierda"""
    cadena  = cadena.lower()
    cadena_invertida = invertir_cadena(cadena)
    resultado = False
    if cadena ==  cadena_invertida:
        resultado = True
    return resultado
cadena = "Holaloh"
print(polindromo(cadena))


#4) Crear una función que reciba como parámetro una cadena y suprima los
#caracteres repetidos.
#Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def suprimir_caracteres_repetidos(cadena:str):
    """Ingresa una cadena, la recorre con un for,
    si encuentra caracteres consecutivos repetidos, 
    realiza una nueva cadena suprimiendo esos caracteres""" #Que sucede con las RR o CC????
    cadena.split()
    nueva_cadena =""
    for i in range(len(cadena)):
        if cadena[i] != cadena[i-1]:
            nueva_cadena += cadena[i]
    return nueva_cadena

cadena = "hooooooolla"
resp = suprimir_caracteres_repetidos(cadena)
print(resp)


#5) Crear una función que reciba una cadena por parámetro y suprima las
#vocales de la misma.
#Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
def suprimir_vocales (cadena:str):
    """Ingresa una cadena, si tiene vocales, las reemplaza por un guion medio"""
    for i in range(len(cadena)):
        if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u":
            cadena = cadena.replace(cadena[i], "-")
    return cadena

cadena = "hoooliia"
respuesta = suprimir_vocales(cadena)
print(respuesta)


#6) Crear una función para contar cuántas veces aparece una subcadena dentro
#de una cadena.
#Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá
#retornar el valor 2


def buscar_subcadena_en_cadena(cadena, subcadena)->int:
    """Ingresan una cadena y una subcadena por parametro.
    busca cuantas veces aparece la subcadena en la cadena"""
    resultado = cadena.count(subcadena)
    return resultado

"""cadena = "El pan del panadero"
subcadena = "pan"
contador = buscar_subcadena_en_cadena(cadena,subcadena)
print(contador)"""



#https://github.com/CamiAilenn/Progra_Uno/blob/main/11_Cadena_de_Caracteres_dos.py



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
def polindromo (cadena:str)-> bool:
    """Ingresa una cadena por parametro.
    Si es un polindromo retorna VERDADERO, sino FALSO.
    Polindromo: Palabra o frase que se lee igual de izquierda a derecha 
    que de derecha a izquierda"""
    cadena.lower()
    resultado = False
    for i in range(len(cadena)):
        if cadena[i] == cadena[len(cadena)-1-i]:
            resultado = True
    return resultado
"""cadena = "Holal oh"
print(polindromo(cadena))"""


#4) Crear una función que reciba como parámetro una cadena y suprima los
#caracteres repetidos.
#Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def suprimir_caracteres_repetidos(cadena:str):
    """Ingresa una cadena, la recorre con un for,
    si encuentra caracteres consecutivos repetidos, 
    realiza una nueva cadena suprimiendo esos caracteres""" #Que sucede con las RR o CC????
    lista = list(cadena)
    for i in range(len(lista)-3):
        if lista[i] == lista[i+1]:
            lista.pop(i)
            suprimir_caracteres_repetidos(lista)
    cadena = str(lista)
    return cadena 

"""cadena = "hoooola"
resp = suprimir_caracteres_repetidos(cadena)
print(resp)"""
#NO ME SALIO, no se como sacar caracteres, no se puede porque es inmutable, pero no se como crear 
# una nueva cadena sin cierto caracter


#5) Crear una función que reciba una cadena por parámetro y suprima las
#vocales de la misma.
#Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
def suprimir_vocales (cadena:str):
    """Ingresa una cadena, si tiene vocales, las elimina"""
    for i in range(len(cadena)):
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            print("hasta aca llegue")



#6) Crear una función para contar cuántas veces aparece una subcadena dentro
#de una cadena.
#Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá
#retornar el valor 2
#Intente hacer una recursiva que busque letra a letra la subcadena en la cadena principal

"""def comparar(cadena, subcadena, i, posicion=0):
    acumulador = 0
    acumulador += 1
    if cadena[i] == subcadena[posicion]:
        comparar(cadena, subcadena, i+1, posicion+1)
    else:
        return acumulador
def buscar_subcadena_en_cadena(cadena:str, subcadena:str)->int:
  #Ingresan una cadena y una sub-cadena por parametro,
   # si la sub-cadena se encuentra en la cadena principal,
    #cuenta cuantas veces esta dentro y retorna la cantidad
    
    for i in range(len(cadena)):
        resultado = comparar(cadena, subcadena, i)
    return resultado"""

def buscar_subcadena_en_cadena (cadena,subcadena):
    if subcadena in cadena:
        print("SI")

#¿¿¿Como cuento las veces que aparece???


cadena = "El pan del panadero"
subcadena = "pan"
print(buscar_subcadena_en_cadena(cadena,subcadena))



#https://github.com/CamiAilenn/Progra_Uno/blob/main/11_Cadena_de_Caracteres_dos.py



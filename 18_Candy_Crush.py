# #Recientemente Candy Crush Saga le pide una variación del juego a U.T.N para 
# su juego de consola con los siguientes requerimientos:
#Dada la siguiente lista de diccionarios
#● lista = [
#● {"piezas":[]},
#● {"piezas":[]},
#● {"piezas":[]},
#● {"piezas":[]}
#● ]
#
#Desarrollar una función que genere números al azar entre 1 y 3, y completar las 
# listas para que queden de la siguiente forma:
# Ej:
# ● [2, 3, 3, 3, 3, 3, 1]
# ● [1, 1, 1, 1, 1, 1, 3]
# ● [3, 1, 2, 3, 1, 1, 1]
# ● [1, 1, 3, 2, 3, 2, 2]
# (los número son generados al azar)
#
#
#Solicitar al usuario una posición (fila y una columna)
#Verificar si, de forma vertical, existen desde esa posición elegida, 
#hacia arriba o hacia abajo 3 números iguales, es decir 3 unos, 3 dos o 3 tres.
#Si existen mostra el mensaje "HA GANADO 10 PUNTOS", sino "SEGUI PARTICIPANDO"
# Utilizar funciones, validar el ingreso de datos

from random import *

def inicializar_lista_de_diccionarios (filas:int, clave:str, valor)->list:
    """Ingresa por parametros la cantidad de filas que tendra la matriz
    ingresa la clave que se repetira en cada fila y y columnas que tendra la matriz.
    Por default la inicializa con ceros, sino el usuario ingresara por parametro"""
    matriz = []
    for i in range(filas):
        filas = {clave:valor}
        matriz += [filas]
    return matriz

def inicializar_lista(len)->list:
    """Ingresa por parametro la cantidad de posiciones que tendra la lista
    la inicializa con 0 en las posiciones"""
    lista = [0] * len
    return lista

def completar_lista_de_diccionarios_con_enteros_aleatorios(lista:list, clave, inicio_random:int, fin_random:int)->list:
    """ingresa por parametro una lista en formato matriz, la recorre 
    y en cada posicion le va agregando un numero entero generando aleatoriamente.
    Por parametro tambien ingresa el rango en que se quiere generar los numeros"""
    for i in range(len(lista)):
        for j in range(len(lista[i][clave])):
            lista[i][clave][j] = randint(inicio_random,fin_random)
    return lista

lista_del_diccionario = inicializar_lista(7)
clave = "Piezas"
inicio_piezas = 1
fin_piezas = 3
lista = inicializar_lista_de_diccionarios(4,clave,lista_del_diccionario)

for i in range(len(lista)):
    print(lista[i])

lista_completa = completar_lista_de_diccionarios_con_enteros_aleatorios(lista, clave, inicio_piezas, fin_piezas)

print(lista_completa[0][clave][3])
for i in range(len(lista_completa)):
    print(lista_completa[i])













#------------------------------------------------------------
def validar_rango(numero, desde, hasta)->float | int:
    """Valida el numero en un rango, y lo pide indefinidamente hasta que este validado
    Una vez validado, lo retorna"""
    while numero< desde or numero > hasta:
        numero = int(input(f"Ingreso, no valido. Ingrese un numero ({desde+1}-{hasta+1}): "))
    return numero


def ingresar_validar_fila(desde=0, hasta=9)->int:
    """Solicita y valida una posicion(fila) al usuario"""
    
    fila = int(input(f"¿En que fila se encuentra? ({desde+1}/{hasta+1})"))
    fila = validar_rango(fila-1, desde, hasta)   
    return fila 

def ingresar_validar_columna(desde=0, hasta=9)->int:
    """Solicita y valida una posicion(columna) al usuario"""
    columna = int(input(f"¿En que columna se encuentra? ({desde+1}/{hasta+1})"))
    columna = validar_rango(columna-1, desde, hasta)
    return columna
    
contador = 1    
"""tablero = inicializar_matriz(4,7)
tablero = completar_matriz_numeros_enteros_aleatorios(inicializar_matriz(4,7), 1, 3)"""
tablero = [[1, 3, 3, 3, 1, 2, 1],
            [1, 3, 3, 2, 2, 3, 2],
            [1, 3, 2, 2, 1, 3, 2],
            [2, 1, 3, 3, 1, 2, 3] ]

for i in range(len(tablero)):
    print(tablero[i])

print("Usted ingresara una posicion")
fila = ingresar_validar_fila(0,3)
columna = ingresar_validar_columna(0,6)
numero = tablero[fila][columna]
print(numero)

if fila == 0:
    for i in range(1, len(tablero)):
        if tablero[i][columna] == numero:
            print(tablero[i][columna])
            contador += 1
elif fila != 0: #pulir esta parte
    for i in range(fila-1, 0, -1):
        if tablero[i][columna] == numero:
            contador += 1
    for i in range(fila+1, len(tablero)):
        if tablero[i][columna] == numero:
            contador += 1

print(contador)
if contador >= 3:
    print("HA GANADO 10 PUNTOS")
else:
    print("SEGUI PARTICIPANDO")
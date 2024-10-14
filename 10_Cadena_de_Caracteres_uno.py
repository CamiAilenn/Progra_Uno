#CADENA DE CARACTERES
#**IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el 
#<número de caracteres> - 1.


#Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
#Debe retornar las veces que la letra está incluida en el texto.
def contador_letras(letra:str, cadena:str)->int:
    """Ingresa por parametro una letra y una cadena.
    Cuenta las veces que esta incluida esa letra en la cadena
    retorna un entero"""
    acumulador = 0
    for i in cadena:
        if letra == i:
            acumulador += 1
    return acumulador
#letra = "o"
#cadena = "Hola como estas tu?"
#print(contador_letras(letra,cadena))


#Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices. 
#Se debe retornar la cadena que va entre las posiciones indicadas por los índices. 
#Si las posiciones no son válidas se debe informar.
def cortar_cadena(cadena:str, inicio:int, fin:int)->str:
    """Slicing. Ingresa una cadena y dos posiciones
    retorna la parte de la cadena que estan entre las posciones ingresadas"""
#    if len(cadena) < inicio or inicio < 0 and len(cadena) > fin:
#       resultado = f"Posiciones de inicio = {inicio} y fin = {fin} invalidas"
    if len(cadena) < inicio or inicio < 0:
        resultado = f"Posicion de inicio = {inicio} invalida. La cadena tiene {len(cadena)} posiciones (0-{len(cadena)-1})"
    elif len(cadena) < fin:
        resultado = f"Posicion de fin = {fin} invalida. La cadena tiene {len(cadena)} posiciones (0-{len(cadena)-1})"       
    else:
        resultado = cadena[inicio:fin]

    return resultado

#cadena = "hola, esta cadena es de prueba"
#print(cortar_cadena(cadena,15,100))


#Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número. 
#Se debe retornar el caracter en la posición indicada por el número si ésta es válida. 

def char_at(cadena:str,posicion:int)->str:
    """Recibe una cadena y una posicion.
    Si en dicha posicion existe un caracter, lo retorna"""
    if len(cadena) < posicion:
        resultado = f"La cadena tiene un indice de posiciones del 0 al {len(cadena)-1}"
    elif len(cadena[posicion]) == 0:
        resultado = print(f"En la posicion {posicion} no existe ningun caracter")
    else:
        resultado = cadena[posicion]
    return resultado

"""cadena = "Hola"
print(char_at(cadena,100))"""



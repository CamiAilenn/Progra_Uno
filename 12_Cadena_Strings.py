import Modulos_y_Paquetes.Funciones_Cami as PAQ
#Ejercicio 1: Desarrollar una función que Invierte el orden de los caracteres en una cadena. 
def invertir_cadena(cadena:str)->str:
    """Ingresa una cadena y la funcion invierte el orden de los caracteres"""
    nueva_cadena = ""
    for i in range(len(cadena)):
        caracter = cadena[len(cadena)-1-i]
        nueva_cadena += caracter
    return nueva_cadena
"""cadena = "Hola Camila"
print(invertir_cadena(cadena))"""

#Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena. 

def suprimir_dobles_espacios(cadena:str):
    """Ingresa una cadena, la recorre con un for,
    si encuentra dos espacios juntos, 
    realiza una nueva cadena suprimiendo esos caracteres"""
    cadena.split()
    nueva_cadena =""
    for i in range(len(cadena)):
        if cadena[i] != cadena[i-1]:
            nueva_cadena += cadena[i]
    return nueva_cadena

def contar_palabras(cadena:str)->int:
    """Ingresa una cadena, le saca los espacios, si lo hay, 
    que se encuentren al comiezo y al final de la misma
    y cuenta cuantas palabras hay, contando los espacios"""
    resultado = cadena.count(" ")
    return resultado

'''cadena = " H o  la  camila como estas ? "
print(contar_palabras(cadena))
cadena = suprimir_dobles_espacios(cadena)
print(contar_palabras(cadena))'''

#Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra 
#en una cadena. 
def reemplazar_palabra(cadena:str, palabra_original:str, palabra_remplazo:str)->str:
    """Ingresa una cadena de caracteres,una palabra (original) que se encuentra en ella,
    la busca, y la reemplaza por otra palabra indicada por parametro tambien(reemplazo)"""
    cadena = cadena.replace(palabra_original, palabra_remplazo)
    return cadena

'''cadena = " Hola  camila como estas ? "
print(reemplazar_palabra(cadena, "camila", "ariel"))'''



#Ejercicio 4: Desarrollar una función que convierta los elementos de lista_peli en una 
#cadena y muestre:  
#ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento 
lista_peli = [ 
                ["Matrix", "El Padrino", "Titanic"], 
                ["Forrest Gump", "Pulp Fiction", "Gladiador"],  
                ["Blade Runner", "El Rey León", "Volver al Futuro"],  
                ["La La Land", "El Gran Lebowski", "Blade Runner"],  
                ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"], 
                ["Harry Potter", "Forrest Gump", "Pulp Fiction"],  
                ["Titanic", "Star Wars", "El Señor de los Anillos"],  
                ["The Truman Show", "The Shape of Water", "The Big Lebowski"],  
                ["Forrest Gump", "The Godfather", "Goodfellas"], 
                ["The Terminator", "The Sixth Sense", "The Great Gatsby"] 
] 


def armar_cadena_de_una_lista(lista:list, separador = ", "):
    """Ingresa una lista y separa la misma con un indicador en el medio, 
    usando el metodo join ingresado por parametro el separador,
    sino por default es una coma"""
    
    for i in range(len(lista)):
        cadena = "Se recomienda ver "
        cadena += separador.join(lista[i])
        print(cadena)

armar_cadena_de_una_lista(lista_peli)

def armar_cadena_de_una_lista(lista:list, introduccion = "Se recomienda ver ", ):
    """Ingresa una lista y separa la misma con un indicador en el medio, 
    recorriendola con dos for, de manera muy particular,
    Ingresa por parametro la introccion"""

    for i in range(len(lista)):
        cadena = introduccion
        for j in range(len(lista[i])):
            if lista[i][j] == lista[i][0]:
                cadena += "\""
                cadena += lista[i][j]
                cadena += "\""                
            elif lista[i][j] != lista[i][-1]:
                cadena += ", \""
                cadena += lista[i][j]
                cadena += "\""
            else:
                cadena += " y \""
                cadena += lista[i][j]
                cadena += "\""                
        print(cadena)

armar_cadena_de_una_lista(lista_peli)



#Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena. 

def capitalizar_palabras(cadena:str):
    """Ingresa una cadena y capitaliza TODAS las palabras de la cadena"""
    cadena = cadena.title()
    return cadena

cadena = "hola camila como estas?"
print(capitalizar_palabras(cadena))


#Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo: 
#Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta 
#la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo, 
#anilina. 

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

#Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número (1 o -1).  
# Se debe retornar el string ordenado de manera #ascendente (si recibió 1 por 
#parámetros) o descendente (si recibió -1) 
#Nota: Determinar parámetros y retornos de manera que las funciones sean 
#genéricas y reutilizables.


def transformar_cadena_en_lista(cadena:str)->list:
    """Ingresa una cadena, convierte todas las letras en minuscula.
    Luego reconoce si es una palabra o una oracion
    y arma una lista con la cadena."""
    lista = []
    cadena.lower()
    if cadena.isalnum():
        for i in range(len(cadena)):
            lista += cadena[i]
    else:
        lista = cadena.split()
    return lista

def transformar_lista_en_cadena(lista:list)->str:
    """Ingresa una lista. Reconoce si son letras o palabras el contenido.
    Luego arma una cadena con la lista"""
    bandera_oracion = False
    for i in range(len(lista)):
        if len(lista[i]) != 1:
            bandera_oracion = True
    if bandera_oracion:
        separador = " "
        cadena = separador.join(lista)
    else:
        separador = ""
        cadena = separador.join(lista)
    return cadena

def ordenar_ascendente (lista:list)->list:
    """Ingresa una lista, la ordena de manera ascendente"""
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                swapear_lista(lista, i, j)
    return lista

def ordenar_descendente (lista:list)->list:
    """Ingresa una lista, la ordena de manera descendente"""
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] < lista[j]:
                swapear_lista(lista, i, j)
    return lista

def swapear_lista(lista:list, posicion_primera:int, posicion_segunda:int):
    """ingresa una lista y dos posiciones por parametro, e intercambia las posiciones
    retorna la nueva lista con las posiciones intercambiadas"""
    aux = lista[posicion_primera]
    lista[posicion_primera] = lista[posicion_segunda]
    lista[posicion_segunda] = aux

def ordenar_cadena_ascendete_descendente(cadena:str, tipo_orden = 1)->str:
    """Ingresa por parametro una cadena y un numero. 
    La cadena pone todas las letras en minuscula, al numero lo valida.
    Si el numero es 1 la cadena se ordenara de manera ascendente,
    si el numero es -1 la cadena se ordenara de manera descendente.
    por default se ordenara de manera ascendente.
    Retornara la cadena ordenada"""
    cadena = cadena.lower()
    lista = transformar_cadena_en_lista(cadena)
    while tipo_orden != 1 and tipo_orden != -1:
        tipo_orden = int(input("Indique correctamente como quiere ordenar la cadena (1 = ascendente / -1 = descendente): "))
    if tipo_orden == 1:
        lista_ordenada = ordenar_ascendente(lista)
    else:
        lista_ordenada = ordenar_descendente(lista)
    cadena_ordenada = transformar_lista_en_cadena(lista_ordenada)
    return cadena_ordenada


cadena = "camila vos bien"
print(ordenar_cadena_ascendete_descendente(cadena, -2))


#Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial,
#los guarde en una lista y la retorne. El programa principal debe invocar a la
#función y mostrar por pantalla el retorno.

def diez_nombres()->list:
    '''Pedira 10  nombres y armara una lista'''
    lista_nombres = []
    for i in range(10):
        nuevo_nombre = str(input("Ingrese un nombre: ").capitalize())
        lista_nombres.append(nuevo_nombre)
    return lista_nombres

nombres = diez_nombres()
print(nombres)

#Opcion dos, universal para cantidad de nombres cualquiera

def lista_nombres(cantidad_de_nombres:int)->list:
    '''Pedira X cantidad de nombres y armara una lista'''
    lista_nombres = []
    for i in range(cantidad_de_nombres):
        nuevo_nombre = str(input("Ingrese un nombre: ").capitalize())
        lista_nombres.append(nuevo_nombre)
    return lista_nombres

cuantos_nombres = 10
nombres = lista_nombres(cuantos_nombres)
print(nombres)


#Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números
#en 0, pida posición y número a guardar al usuario, lo guarde en una lista 
#en la posición solicitada aleatoriamente y la retorne. El programa principal
#debe invocar a la función y mostrar por pantalla el retorno.


def agregar_numero_aleatorio(cantidad:int)->list:
    '''Pide al usuario el ingreso de una posicion y le asigna un numero el mismo usuario'''
    lista_numeros = [0]*cantidad
    ingresar_otro = "s"
    while ingresar_otro == "s":
        posicion = int(input("Ingrese una posicion de 0 a 9 ")) 
        nuevo_numero = int(input("Ingrese un numero: "))
        lista_numeros[posicion] = nuevo_numero
        ingresar_otro = input("Desea ingresar otro s/n: ").lower()

    return lista_numeros

ingresos = 10
numeros = agregar_numero_aleatorio(ingresos)
print(numeros)


#Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango 
#especificado, validar los números solicitados dentro de ese rango, guardar
#en una lista y retornarla. El programa principal debe invocar a la función
#y mostrar por pantalla el retorno.

def diez_numeros():
       for i in range(10):
            numero = int(input("Ingrese un numero(0-100): "))
            while numero <= 0 or numero >= 100:
                numero = int(input("Ingreso, no valido. Ingrese un numero: "))

resultado = diez_numeros()
print(resultado)


#Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de 
#números y un número especificado. La misma debe buscar el número especificado
#en la lista y retornar “True” si existe.

def buscar_numero_en_lista(lista:list, numero:int)-> bool:
    '''Ingresa una lista y numero por parametro,
    busca en la lista si existe ese numero
    retorna un booleano'''
    resultado = False
    for i in range (len(lista)):
        if numero == lista[i]:
            resultado = True
    if resultado:
        return True
    else:
        return False
        


#Ejercicio 5: Dadas las siguientes listas:
#Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria",
#"Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
#edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
#Desarrollar una función que reciba por parámetro la lista de edades, busque
#a las personas de menor edad (puede ser más de una) y las retorne. El programa
#principal deberá mostrar nombre y edad de los menores.


nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def lista_edad_menores(edad:list)->list:
    '''Ingresan lista de edades parametro 
    encuentra los menores y retorna una lista con las posiciones 
    para luego decir nombre y edad,u otros datos '''
    menores = []    
    menor = edad[0]
    for e_edades in range (len(edad)):
        if edad[e_edades] <= menor:
            menor = edad[e_edades]
    for i in range (len(edad)):
            if edad[i] == menor:
                 menores.append(i)
    return menores

resultado = lista_edad_menores(edades)
for i in range(len(resultado)):
     print(nombres[resultado[i]])


#Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo 
#listas_personas.py. Importar los nombres a una lista. Realizar una función que 
#muestre los mismos.
from Archivo_con_listas import *

def mostrar_lista(lista:list):
    "Muestra una lista con un for"
    for i in range (len(lista)):
        print(lista[i])

nombres_c = nombres
resultado = mostrar_lista(nombres_c)
print(resultado)


#Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de 
#compras on-line recientemente lanzado al mercado para ello necesita un programa 
#que le permita acceder a los datos relevados.
#Realizar una función con el siguiente Menú de Opciones:
#1-Importar listas
#2-Listar los datos de los usuarios de México
#3-Listar los nombre, mail y teléfono de los usuarios de Brasil
#4-Listar los datos del/los usuario/s más joven/es
#5-Obtener un promedio de edad de los usuarios
#6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
#7-Listar los datos de los usuarios de México y Brasil cuyo código postal 
#sea mayor a 8000
#8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 
#años.




#Ejercicio 8: Crear una función para cada opción de menú.
#Ejercicio 9: Desarrollar las funciones en una biblioteca.
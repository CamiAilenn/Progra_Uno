#FUNCIONES y LISTAS
#Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los 
#guarde en una lista y la retorne. El programa principal debe invocar a la función y
#mostrar por pantalla el retorno.

def diez_nombres()->list:
    """Pide diez nombres secuencialmente los guarda en una lista.
    Retorna la misma"""
    lista_nombres = []
    for i in range(10):
        nombres = str(input("Ingrese un nombre: ")).capitalize()
        lista_nombres.append(nombres)
    return lista_nombres

"""resultado = diez_nombres()
for e_resultados in resultado:
    print(e_resultados)"""



#Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida 
#posición y número a guardar al usuario, lo guarde en una lista en la posición 
#solicitada aleatoriamente y la retorne. El programa principal debe invocar a la 
#función y mostrar por pantalla el retorno.
#Modifique para que el indice coincida con la ubicacion que ocupa
def diez_numeros()->list:
    """Inicializa una lista de 10 numeros en 0.
    Solicita al usuario posicion y numero a asignar"""
    lista = [0]*10
    continuar = "s"
    contador = 0
    while continuar == "s" or contador == 10:
        contador += 1
        posicion = int(input("Indique la posicion (1-10): "))
        while posicion <= 0 or posicion > 10:
            posicion = int(input("Posicion invalida. Indique la posicion (1-10): "))
        while lista[posicion - 1] != 0:
            print(f"La posicion {posicion} esta ocupada por el numero{lista[posicion - 1]}")
            posicion = int(input("Ingrese otra posicion: "))
        numero = int(input("Ingrese numero: "))
        continuar = str(input("¿Desea continuar? (s/n) ")).lower()
        lista[posicion - 1] = numero
    return lista

"""resultado = diez_numeros()
for i in range(len(resultado)):
    print(f"En la posicion {i+1} se encuenta el numero: {resultado[i]}")
"""
#Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango 
#especificado, validar los números solicitados dentro de ese rango, guardar en una 
#lista y retornarla. El programa principal debe invocar a la función y mostrar por 
#pantalla el retorno.
#Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números 
#y un número especificado. La misma debe buscar el número especificado en la lista 
#y retornar “True” si existe.
#Ejercicio 5: Dadas las siguientes listas:
#Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
#ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
#edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
#Desarrollar una función que reciba por parámetro la lista de edades, busque a las 
#personas de menor edad (puede ser más de una) y las retorne. El programa 
#principal deberá mostrar nombre y edad de los menores.
#Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo 
#listas_personas.py. Importar los nombres a una lista. Realizar una función que 
#muestre los mismos.



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
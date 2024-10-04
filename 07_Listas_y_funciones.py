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
    return resultado
   


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


from Archivo_con_listas import *
import Modulos_y_Paquetes.Funciones_Cami as PAQ


#1-Importar listas
nombres_copia = nombres
telefonos_copia = telefonos
mails_copia = mails
address_copia = address
postalZip_copia = postalZip
region_copia = region
country_copia = country
edades_copia = edades

def mostrar_primera_fila():
    '''Muestra la primera fila con los datos que contiene de cada columna'''
    print("""Nombre y apellido    telefono            mail            direccion         codigo postal   region    pais   edad""")     

def mostrar_datos_una_posicion(posicion:int, nombre:list, telefono:list, mail:list, address:list, 
                            postalZip:list, region:list, country:list, edad:list):
    """Muestra los datos del usuario en la posicion ingresada por parametro"""
    print(nombre[posicion],"  ", telefono[posicion], "  ",mail[posicion], "  ",
          address[posicion],"  ", postalZip[posicion], "  ", region[posicion], "  ",
          country[posicion], "  ", edad[posicion])

def mostrar_datos_de_lista_de_posiciones(lista:list, nombre:list, telefono:list, 
                                         mail:list, address:list, postalZip:list, 
                                         region:list, country:list, edad:list):
    """Muestra los datos usuarios de una lista ingresada por parametro"""
    if len(lista) == 0:
        print("No hay datos en la lista")
    else:
        mostrar_primera_fila()
        for i in range(len(lista)):
            mostrar_datos_una_posicion(lista[i], nombre, telefono, mail, address, postalZip, region, country, edad)

def mostrar_nombre_mail_telefono(lista, nombre:list, telefono:list, mail:list):
    "Muestra nombre-mail-telefono de los usuarios del pais ingresado por un input"
    print("Nombre y apellido          mail              telefono        pais  ")   
    if len(lista) == 0:
        print("No hay datos en la lista")
    else:
        for i in range(len(lista)):
            print(nombre[lista[i]],"   ",mail[lista[i]] , "   ", telefono[lista[i]],)

#2-Listar los datos de los usuarios de México

def datos_usuarios_por_pais_parametro(pais, nombre:list, telefono:list, mail:list, address:list, 
                            postalZip:list, region:list, country:list, edad:list ):
    "Muestra los datos de los usuarios del pais indicado por parametro"

    print("Nombre y apellido    telefono            mail            direccion          codigo postal   region    pais   edad")   
    for i in range (len(country)):
        if pais == country[i]:
            mostrar_datos_una_posicion(i, nombre, telefono, mail, address, postalZip, region, country, edad)

pais ="Mexico"
datos_usuarios_por_pais_parametro(pais, nombres_copia, telefonos_copia, mails_copia, 
                                  address_copia, postalZip_copia, region_copia, country_copia, edades_copia)


#Lo realice generico, para que muestre los datos de los usuarios
#del pais que ingrese el usuario.
def datos_usuarios_por_pais(nombre:list, telefono:list, mail:list, address:list, 
                            postalZip:list, region:list, country:list, edad:list ):
    "Muestra los datos de los usuarios del pais ingresado por un input"

    pais = str(input("Ingrese el PAIS, de las personas que quiere obtener datos: ")).capitalize()
    mostrar_primera_fila()
    for i in range (len(country)):
        if pais == country[i]:
            mostrar_datos_una_posicion(i, nombre, telefono, mail, address, postalZip, region, country, edad)

#datos_usuarios_por_pais(nombres_copia, telefonos_copia, mails_copia, address_copia, postalZip_copia, region_copia, country_copia, edades_copia)



#3-Listar los nombres, mail y teléfono de los usuarios de Brasil
#Lo realice generico, para que muestre los datos de los usuarios
#del pais que ingrese el usuario.
def mostrar_nombre_mail_telefono_por_pais(nombre:list, telefono:list, mail:list, country:list):
    "Muestra nombre-mail-telefono de los usuarios del pais ingresado por un input"
    pais = str(input("Ingrese el PAIS, de las personas que quiere obtener datos: ")).capitalize()
    print("Nombre y apellido          mail              telefono        pais  ")   
    for i in range (len(country)):
        if pais == country[i]:
            print(nombre[i],"   ",mail[i] , "   ", telefono[i],"   ", country[i])

#mostrar_nombre_mail_telefono_por_pais(nombres_copia, telefonos_copia, mails_copia, country_copia)


#4-Listar los datos del/los usuario/s más joven/es
    
def edad_usuario_mas_joven(edades:list)->int:
    """Busca la edad del usuario mas joven"""
    edad_menor = edades[0]
    for i in range(len(edades)):
        if edades[i] < edad_menor:
            edad_menor = edades[i]
    return edad_menor
#print(edad_usuario_mas_joven(edades))

def armar_lista_usuarios_jovenes(edades:list)->list:
    """Arma una lista con las posiciones de los usuarios mas jovenes"""
    edad_menor = edad_usuario_mas_joven(edades)
    lista_posiciones_usuarios_jovenes = []
    for i in range(len(edades)):
        if edades[i] == edad_menor:
            lista_posiciones_usuarios_jovenes.append(i)
    return lista_posiciones_usuarios_jovenes
#print(armar_lista_usuarios_jovenes(edades))

#print(mostrar_datos_de_lista_de_posiciones(armar_lista_usuarios_jovenes(edades), nombres, telefonos, mails, address, postalZip, region, country, edades))

#5-Obtener un promedio de edad de los usuarios
def promedio_edades(edades:list):
    """Ingresa una lista por parametro y calcula el promedio
    Retorna el promedio"""
    acumulador = 0
    promedio = 0
    for i in range(len(edades)):
        acumulador += edades[i]
    promedio = acumulador / len(edades)
    return promedio

#resultado = promedio_edades(edades_copia)
#print(resultado)



#6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
def edad_usuario_mas_grande(edades:list)->int:
    """Busca la edad del usuario mas grande"""
    edad_mayor = edades[0]
    for i in range(len(edades)):
        if edades[i] > edad_mayor:
            edad_mayor = edades[i]
    return edad_mayor
#print(edad_usuario_mas_grande(edades))

def armar_lista_posicion_usuarios_mayores(edades:list)->list:
    """Arma una lista con las posiciones de los usuarios mas mayores"""
    edad_mayor = edad_usuario_mas_grande(edades)
    lista_posiciones_usuarios_mayores = []
    for i in range(len(edades)):
        if edades[i] == edad_mayor:
            lista_posiciones_usuarios_mayores.append(i)
    return lista_posiciones_usuarios_mayores
#print(armar_lista_posicion_usuarios_mayores(edades))


def armar_lista_usuarios_mayores_por_pais(pais:str, paises:list,edades:list)->list:
    """Encuentra a los usuarios de determinado pais ingresado por parametro 
    y muestra los datos de los de de mayor edad"""
    edad_mayor = edad_usuario_mas_grande(edades)
    lista_posiciones_por_pais_mayores = []
    for i in range(len(paises)):
        if paises[i] == pais:
            if edades[i] == edad_mayor:
                lista_posiciones_por_pais_mayores.append(i)
    return lista_posiciones_por_pais_mayores
   
mostrar_datos_de_lista_de_posiciones(armar_lista_usuarios_mayores_por_pais("Brasil", country_copia, edades_copia), nombres, telefonos, mails, address, postalZip, region, country, edades)


#7-Listar los datos de los usuarios de México y Brasil cuyo código postal 
#sea mayor a 8000

'''def armar_lista_posiciones_mayores_a_valor (minimo:int, lista:list)->list:
    """Recibe un minimo y una lista por parametro, 
    retorna una lista con las posiciones que tienen un numero mayor al indicado"""
    lista_posiciones_mayores = []
    for i in range(len(lista)):
        if lista[i] >= minimo:
            lista_posiciones_mayores.append(i)
    return lista_posiciones_mayores'''
#print(armar_lista_posiciones_mayores_a_valor(8000, postalZip_copia))


def armar_lista_posiciones_usuarios_paises_mayor_codigo_postal(pais:list, codigo_postal:list)->list:
    """Busca usuarios de dos paises y luego busca que el codigo postal 
    sea mayor a un minimo. 
    Retorna una lista con las posiciones que cumplan las dos condiciones"""
    pais_uno = "Mexico"
    pais_dos = "Brasil"
    lista_posiciones_usuarios_paises_mayores = []
    for i in range (len(pais)):
        if pais[i] == pais_uno or pais [i] == pais_dos:
            if codigo_postal[i] > 8000:
                lista_posiciones_usuarios_paises_mayores.append(i)
    return lista_posiciones_usuarios_paises_mayores

mostrar_datos_de_lista_de_posiciones(armar_lista_posiciones_usuarios_paises_mayor_codigo_postal(country_copia, postalZip_copia), nombres, telefonos, mails, address, postalZip, region, country, edades)

#8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.

def mostrar_nombre_mail_telefono_por_pais_mayores_edad(nombre:list, telefono:list, mail:list, country:list, edad:list):
    """Muestra nombre-mail-telefono de los usuarios del pais ingresado por un input
    y valida que sean mayores de edad"""
    pais = str(input("Ingrese el PAIS, de las personas que quiere obtener datos: ")).capitalize()
    print("Nombre y apellido          mail              telefono        pais  ")   
    for i in range (len(country)):
        if pais == country[i]:
            if edad[i] >= 40:
                print(nombre[i],"   ",mail[i] , "   ", telefono[i],"   ", country[i])

#mostrar_nombre_mail_telefono_por_pais_mayores_edad(nombres_copia,telefonos_copia,mails_copia,country_copia,edades_copia)
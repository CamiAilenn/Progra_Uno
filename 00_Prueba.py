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

from Archivo_con_listas import *

#1-Importar listas
nombres_copia = nombres
telefono_copia = telefonos
mails_copia = mails
address_copia = address
postalZip_copia = postalZip
region_copia = region
country_copia = country
edades_copia = edades

#2-Listar los datos de los usuarios de México
def datos_usuarios_por_pais(nombre:list, telefono:list, mail:list, address:list, postalZip:list, region:list, country:list, edad:list ):
    "Muestra los datos de los usuarios del pais ingresado por un input"

    pais = str(input("Ingrese el PAIS, de las personas que quiere obtener datos: ")).capitalize()
    print("Nombre y apellido    telefono            mail            direccion          codigo postal   region    pais   edad")   
    for i in range (len(country)):
        if pais == country[i]:
            print(nombre[i],"  ", telefono[i], "  ",mail[i], "  ",address[i],"  ", postalZip[i], "  ", region[i], "  ", country[i], "  ", edad[i])
datos_usuarios_por_pais(nombres_copia, telefono_copia, mails_copia, address_copia, postalZip_copia, region_copia, country_copia, edades_copia)



#3-Listar los nombres, mail y teléfono de los usuarios de Brasil

def mostrar_nombre_mail_telefono_por_pais(nombre:list, telefono:list, mail:list, country:list):
    "Muestra nombre-mail-telefono de los usuarios del pais ingresado por un input"
    pais = str(input("Ingrese el PAIS, de las personas que quiere obtener datos: ")).capitalize()
    print("Nombre y apellido          mail              telefono        pais  ")   
    for i in range (len(country)):
        if pais == country[i]:
            print(nombre[i],"   ",mail[i] , "   ", telefono[i],"   ", country[i])

mostrar_nombre_mail_telefono_por_pais(nombres_copia, telefono_copia, mails_copia, country_copia)


#4-Listar los datos del/los usuario/s más joven/es
#5-Obtener un promedio de edad de los usuarios
#6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
#7-Listar los datos de los usuarios de México y Brasil cuyo código postal 
#sea mayor a 8000
#8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 
#años.




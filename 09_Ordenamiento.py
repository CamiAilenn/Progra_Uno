#ORDENAMIENTOS
#Ejercicio 1: Dadas las siguientes listas:
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
#Desarrollar una función que realice el ordenamiento de las listas por nombre de 
#manera ascendente.

def swapear_lista(lista:list, posicion_primera:int, posicion_segunda:int)->list:
    """ingresa una lista y dos posiciones por parametro, e intercambia las posiciones
    retorna la nueva lista con las posiciones intercambiadas"""
    aux = lista[posicion_primera]
    lista[posicion_primera] = lista[posicion_segunda]
    lista[posicion_segunda] = aux


def ordenar_ascendente_dos_listas(lista_uno:list,lista_dos:list = []):
    """Ordena de manera ascendente dos listas anidadas, a partir de la primera"""
    for i in range(len(lista_uno)-1):
        for j in range(i+1,len(lista_uno)):
            if lista_uno[i] > lista_uno[j]:
              swapear_lista(lista_uno, i, j)
              if len(lista_dos) != 0:
                  swapear_lista(lista_dos, i, j)


ordenar_ascendente_dos_listas(Nombres, Edades)
print("""Nombres:                 |   Edades:    
-------------------------------------""")
for i in range(len(Nombres)):
    print(f"{Nombres[i]:<{25}}|    {Edades[i]:<{5}}") 



#Ejercicio 2: Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
#Desarrollar una función que realice el ordenamiento de las listas por nombre de 
#manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera 
#descendente.

def ordenar_ascendente_y_descendente(lista_uno:list,lista_dos:list):
    """Ordena de manera ascendente dos listas anidadas, a partir de la primera"""
    for i in range(len(lista_uno)-1):
        for j in range(i+1,len(lista_uno)):
            if lista_uno[i] > lista_uno[j]:
              swapear_lista(lista_uno, i, j)
              swapear_lista(lista_dos, i, j)
            if lista_uno[i] == lista_uno[j]:
                if lista_dos[i] < lista_dos[j]:
                    swapear_lista(lista_uno, i, j)
                    swapear_lista(lista_dos, i, j)


ordenar_ascendente_y_descendente(Nombres, Puntos)

print("""Nombres:                 |   Edades:    
-------------------------------------""")
for i in range(len(Nombres)):
    print(f"{Nombres[i]:<{25}}|    {Puntos[i]:<{5}}") 

#Ejercicio 3: Dadas las siguientes listas:
Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa", "Ramirez", "Perez", "Lopez", "Arregui", "Mitre", "Andrade", "Loza" , "Antares" , "Roca", "Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
#Desarrollar una función que realice el ordenamiento de las listas por apellido de 
#manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera 
#ascendente, si el nombre también es el mismo, debe ordenar por nota de manera 
#descendente.
def ordenar_ascendente_ascendente_descendente(lista_uno:list,lista_dos:list,lista_tres:list):
    """Ordena de manera ascendente tres listas anidadas, 
    si se repiten en la primera, lo hace por la segunda,
    si se repiten en la segunda tambien, lo hara de manera descendente por la tercera"""
    for i in range(len(lista_uno)-1):
        for j in range(i+1,len(lista_uno)):
            if lista_uno[i] > lista_uno[j]:
              swapear_lista(lista_uno, i, j)
              swapear_lista(lista_dos, i, j)
              swapear_lista(lista_tres, i, j)
            if lista_uno[i] == lista_uno[j]:
                if lista_dos[i] > lista_dos[j]:
                    swapear_lista(lista_uno, i, j)
                    swapear_lista(lista_dos, i, j)
                    swapear_lista(lista_tres, i, j)
                if lista_dos[i] == lista_dos[j]:
                    if lista_tres[i] < lista_tres[j]:
                        swapear_lista(lista_uno, i, j)
                        swapear_lista(lista_dos, i, j)
                        swapear_lista(lista_tres, i, j)
    return lista_uno, lista_dos, lista_tres
ordenar_ascendente_ascendente_descendente(Apellidos, Estudiantes, Nota)
print("""Apellido       |     Nombre      |     Nota   
--------------------------------------------------""")
for i in range(len(Apellidos)):
    print(f"{Apellidos[i]:<{15}}|      {Estudiantes[i]:<{11}}|      {Nota[i]:<{5}}")


#Ejercicio 4: Una startup desea analizar las estadísticas de los usuarios de su sitio de 
#compras on-line recientemente lanzado al mercado para ello necesita un programa 
#que le permita acceder a los datos relevados.
#Agregar los siguientes puntos al Menú de Opciones:
#1-Importar listas
#2-Listar los datos de los usuarios de México
#3-Listar los nombre, mail y teléfono de los usuarios de Brasil
#4-Listar los datos del/los usuario/s más joven/es
#5-Obtener un promedio de edad de los usuarios
#6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
#7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea 
#mayor a 8000
#8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 
#años.
#9-Listar los datos de los usuarios de México ordenados por nombre
#10-Listar los datos del/los usuario/s más joven/es ordenados por edad de 
#manera ascendente (Si la edad se repite, ordenar por nombre de manera 
#ascendente)
#11-Listar los datos de los usuarios de México y Brasil cuyo código postal 
#sea mayor a 8000 ordenado por nombre y edad de manera descendente
#Ejercicio 8: Crear una función para cada opción de menú.
#Ejercicio 9: Desarrollar las funciones en una biblioteca.
#Nota: No se podrá acceder a ninguna opción de menú si no se realizó la importación 
#de las listas.

#https://github.com/CamiAilenn/Progra_Uno/blob/main/09_Ordenamiento.py
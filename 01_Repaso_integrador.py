#Tabla de Posiciones de Torneo de Ping-Pong
#Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
#Los datos que se cargarán son:
#Nombre del jugador
#Edad (validar)
#Cantidad de puntos (validar-número entero positivo, hasta 60).
#Número de partidos ganados (validar-número entero positivo, hasta 35).
#Tipo de saque ("plano", "liftado", "cortado")
#Categoría ("elite", "experto", "avanzado")
#Se necesita saber
#Tema A:
#1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
#inclusive.
#2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
#3-Porcentaje de jugadores de categoría "experto".
#4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
#5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite"

otro_ingreso = "s"
contador_elite_plano = 0
menor_edad = 120
nombre_menor_edad = 0
categoria_menor_edad = 0
contador_experto = 0
contador = 0
porcentaje_experto = 0
acumulador_edad_avanzado = 0
contador_avanzado = 0
promedio_edad_avanzado = 0
cont_tipo_saque_plano_elite = 0
cont_tipo_saque_liftado_elite = 0
cont_tipo_saque_cortado_elite = 0

while otro_ingreso == "s":
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    while edad < 18 or edad > 120:
        edad = int(input("Edad no valida. Ingrese la edad: "))
    
    cantidad_puntos = int(input(" ¿Cuantos puntos obtuvo (1 - 60)? "))
    while cantidad_puntos <= 0 or cantidad_puntos > 60:
        cantidad_puntos = int(input("Dato ingresado no valido. ¿Cuantos puntos obtuvo (1 - 59)? "))

    partidos_ganados = int(input("¿Cuantos partidos gano? (1 - 35)"))
    while partidos_ganados <=0 or partidos_ganados > 35:
        partidos_ganados = int(input("Dato ingresado no valido. ¿Cuantos partidos gano (1 - 35)? "))
    
    tipo_de_saque = input ("Indique tipo de saque (plano - liftado - cortado) ").lower()
    while tipo_de_saque != "plano" and tipo_de_saque != "liftado" and tipo_de_saque != "cortado":
        tipo_de_saque = input ("Dato no valido. Indique tipo de saque (plano - liftado - cortado) ").lower()

    categoria = input("Categoria a la que pertenece (elite - experto - avanzado) ").lower()
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("Dato no valido. Categoria a la que pertenece (elite - experto - avanzado) ").lower()

    if categoria == "elite":
        if tipo_de_saque == "plano":
            cont_tipo_saque_plano_elite += 1
            if edad > 19 and edad < 25:
                contador_elite_plano += 1
        elif tipo_de_saque == "cortado":
            cont_tipo_saque_cortado_elite += 1
        else:
            cont_tipo_saque_liftado_elite += 1
    elif categoria == "experto":
        contador_experto += 1
    else:
        contador_avanzado += 1
        acumulador_edad_avanzado += edad

    if menor_edad > edad:
        menor_edad = edad
        if cantidad_puntos > 50:
            nombre_menor_edad = nombre
            categoria_menor_edad = categoria
            

    contador += 1
    otro_ingreso = input("¿Desea realizar otro ingreso? (s/n) ").lower()
    while otro_ingreso != "s" and otro_ingreso != "n":
        otro_ingreso = input("Dato ingresado no valido ¿Desea realizar otro ingreso? (s/n) ").lower()


#Ejercicio 1
print(contador_elite_plano, "es la cantidad de jugadores de elite, con saque plano, entre 19 y 25 años")

#Ejercicio 2
print(nombre_menor_edad, categoria_menor_edad, "es el nombre y la categoria respectivamente, del menor que tiene mas de 50 puntos")

#Ejercicio 3
porcentaje_experto = contador_experto * 100 / contador
print(porcentaje_experto, "% es el porcentaje de jugadores de categoria experto")

#Ejercicio 4
if contador_avanzado != 0:
    promedio_edad_avanzado = acumulador_edad_avanzado / contador_avanzado
    print(promedio_edad_avanzado, "Es el promedio de edad de los jugadores avanzados")
else:
    print("No hay jugadores avanzados")

#Ejercicio 5:

if cont_tipo_saque_liftado_elite > cont_tipo_saque_plano_elite and cont_tipo_saque_liftado_elite > cont_tipo_saque_cortado_elite:
    print("el saque mas usado en la categoria elite es el LIFTADO")
elif cont_tipo_saque_plano_elite > cont_tipo_saque_cortado_elite:
    print("el saque mas usado en la categoria elite es el PLANO")
else:
    print("el saque mas usado en la categoria elite es el CORTADO")

#https://onlinegdb.com/JlX4V1-rr

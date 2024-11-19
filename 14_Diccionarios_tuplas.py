jugadores = [
    {"nombre": "Ana", "edad": 43, "puntos":[10,12,14]},  
    {"nombre": "Juan", "edad": 32, "puntos":[12,10,11]},  
    {"nombre": "Pedro", "edad": 28, "puntos":[9,15,11]},
    {"nombre": "Sol", "edad": 31, "puntos":[11,8,15]}
]

#Buscar el menor de edad y printear el nombre 
menor_nombre = jugadores[0]["nombre"]
menor_edad = jugadores[0]["edad"]
for e_jugadores in jugadores:
    if e_jugadores["edad"] < menor_edad:
        menor_edad = e_jugadores["edad"]
        menor_nombre = e_jugadores["nombre"]

print("El jugador de menor edad es: ", menor_nombre)

#Acumular los puntos de cada jugador
lista_puntos_acumulados = []
for jugador in range(len(jugadores)):
    acumulador = 0 
    lista_puntos_acumulados.append(jugador["nombre"])
    for e_puntos in e_jugadores["puntos"]:
        acumulador += e_puntos
    lista_puntos_acumulados.append
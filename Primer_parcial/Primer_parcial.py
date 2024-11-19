def encontrar_numero(lista:list, entero:int)->int:
    """Ingresa una lista y un numero entero.
    Recorre la lista y busca el numero entero ingresado en la lista 
    y retorna la cantidad de veces que lo encuentra"""
    acumulador_entero = 0
    for i in range(len(lista)):
        if lista[i] == entero:
            acumulador_entero += 1
    return acumulador_entero

def solicitar_numero_entero():
    """Solicita un numero"""
    entero = int(input("Ingrese un entero: "))

    return entero

def validar_rango(numero, desde = 1, hasta = 9)->int:
    """Valida un numero en un rango, si no ingresan los parametros
    por default valida desde el 1 al 9, una vez validado lo retorna"""
    while numero <= desde or numero >= hasta:
        numero = input(f"Numero no valido, ingrese otro numero entre {desde} y {hasta}: ")
    
    return numero


lista = [1,0,5,6,7,1,3,6,7,9,7,4,1,2,0,9]
numero = solicitar_numero_entero ()
numero_validado = validar_rango(numero)
resultado = encontrar_numero(lista,numero_validado)
print(resultado)

#https://onlinegdb.com/grCOsGdIO

#-----------------------------------------------------------------------------------------
#Ejercicio 2

def verificar_coordenadas(tablero:list, x:int, y:int)->bool:
    """Ingresa por parametro una matriz, posicion de fila y columna.
    Si en la posicion indicada hay un numero distinto a cero retorna True
    Si en la posicion indicada hay un cero retorna un false"""
    if tablero[x][y] == 1: #Tendria q haber puesto =! 0
        resultado = True
    else:
        resultado = False
    return resultado

tablero = [[0, 0, 1, 0, 0],
           [0, 1, 0, 1, 0],
           [1, 0, 0, 1, 0],
           [0, 0, 1, 0, 1],
           [0, 0, 0, 0, 1]]
continuar = "s"
contador = 0
while continuar == "s":
    fila = int(input("Ingrese una coordinada para la fila (0-4): "))
    while fila < 0 or fila > 4:
        fila = int(input("Ingreso no valido. Ingrese una coordinada para la fila (0-4): "))

    columna = int(input("Ingrese una coordinada para la columna (0-4): "))
    while columna < 0 or columna > 4:
        columna = int(input("Ingreso no valido. Ingrese una coordinada para la columna (0-4): "))


    if verificar_coordenadas(tablero, fila, columna):
        print("Hundido")
        contador += 1
        tablero [fila][columna] = 0   #Esto cambia a cero la posicion, porque el barco ya fue hundido
                                    # En otra situacion validaria para que la persona no ingrese la misma posicion dos veces
    else:
        print("Agua")

    continuar = input("¿Desea continuar? (s/n) ")

if contador == 0:
    print("Usted no ha hundido ningun barco :(")
else:
    print(f"MUY bien!!! Usted ha hundido {contador} barcos!!!")




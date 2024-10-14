def mostrar_menu_almacen()->int:
       """Muestra el menu de opciones del almacen
       Retorna la opcion ingresada por el usuario"""
       opcion = int(input("""
        Opcion 1: Alta de productos
        Opcion 2: Baja de productos
        Opcion 3: Modificar productos
        Opcion 4: Listar productos.
        Opcion 5: Listar productos ordenado por nombre
        Opcion 6: Salir

        Ingrese la opcion deseada: """))
       return opcion

def alta_productos(lista:list):
       """Ingresa lista por parametro y da de alta un producto,
       si la ubicacion que indica esta vacia"""
       producto = str(input("¿Que producto desea ingresar? ")).capitalize()
       cantidad = int(input("¿Cantidad de productos? "))
       while cantidad < 0 or cantidad > 1000:
             cantidad = int(input("DATO NO VALIDO ¿Cantidad de productos? "))
       fila = int(input("¿En que fila se encuentra? "))
       while fila <= 0 or fila > 3:
             fila = int(input("DATO NO VALIDO ¿En que fila se encuentra? "))
       
       columna = int(input("¿En que columna se encuentra? "))
       while columna <= 0 or columna > 5:
             columna = int(input("DATO NO VALIDO ¿En que columna se encuentra? "))
       if len(lista[fila-1][columna-1]) == 0:
             lista[fila-1][columna-1] = [producto, cantidad, [fila, columna]]
       else:
             print("Ubicacion ocupada por otro producto, volvera al menu principal")
       for i in range(len(lista)):
            print(lista[i])



def baja_productos(lista:list):
       """Ingresa una lista, pide al usuario que indique fila/columna del
       producto que dara de baja. En su lugar se reemplazara por una lista vacia []"""
       
       print("Usted dara de baja un producto.")
       fila = int(input("¿En que fila se encuentra? "))
       while fila <= 0 or fila > 3:
             fila = int(input("DATO NO VALIDO ¿En que fila se encuentra? "))
       columna = int(input("¿En que columna se encuentra? "))
       while columna <= 0 or columna > 5:
             columna = int(input("DATO NO VALIDO ¿En que columna se encuentra? "))
       if len(lista[fila-1] [columna-1]) != 0:
             lista[fila-1] [columna-1] =[]
       else:
             print("No hay producto para dar de baja. Volvera al menu principal.") 
       
       for i in range(len(lista)):
            print(lista[i])


def modificar_productos(lista:list):
       
      print("Usted dara de modificarala cantidad y/o ubicacion de un producto.")
      fila_original = int(input("¿En que fila se encuentra? "))
      while fila_original <= 0 or fila_original > 3:
            fila_original = int(input("DATO NO VALIDO ¿En que fila se encuentra? "))
      columna_original = int(input("¿En que columna se encuentra? "))
      while columna_original <= 0 or columna_original > 5:
            columna_original = int(input("DATO NO VALIDO ¿En que columna se encuentra? "))

      if len(lista[fila_original-1][columna_original-1]) == 0:
            print("No hay producto para modificar")
      else:
            print("Usted modificara el producto", lista[fila_original-1][columna_original-1][0])

            modificar_cantidad = str(input("¿Quiere modificar la cantidad? s/n")).lower()
            if modificar_cantidad == "s":
                cantidad = int(input("¿Cual es la nueva cantidad? "))
                while cantidad < 0 or cantidad > 1000:
                    cantidad = int(input("DATO NO VALIDO ¿Cantidad de productos? "))
                lista[fila_original - 1][columna_original - 1][1] = cantidad
            print("Cantidad MODIFICADA")

            modificar_ubicacion = str(input("¿Quiere modificar la ubicacion? s/n")).lower()
            if modificar_ubicacion == "s":
                fila = int(input("¿A que fila lo movera? "))
                while fila <= 0 or fila > 3:
                    fila = int(input("DATO NO VALIDO ¿A que fila lo movera? "))
                columna = int(input("¿A que columna lo movera? "))
                while columna <= 0 or columna > 5:
                    columna = int(input("DATO NO VALIDO ¿A que columna lo movera? "))
       
            if len(lista[fila - 1][columna - 1]) == 0:
                lista[fila - 1][columna - 1] = [lista[fila_original - 1][columna_original - 1][0], cantidad, [fila, columna]]
                lista[fila_original - 1][columna_original - 1] = []
            else:
                print("Ubicacion ocupada por otro producto, volvera al menu principal")
       
      for i in range(len(lista)):
            print(lista[i])



def listar_productos(lista:list):
      """Ingresa una lista por parametro y muestra la misma en forma de matriz"""
      for i in range (len(lista)):
            for j in range (len(lista[i])):
                  print(lista[i][j], end ="      ")
            print(" ")
      
'''      print("Otra alternativa")
      for i in range (len(lista)):
            print(f"{lista[i][0]:<{15}}|   {lista[i][1]:<{15}}|   {lista[i][2]:<{15}}")'''



def armar_lista_con_produtos(lista:list)->list:
      """Arma una nueva lista unicamente con los datos que contenta la ingresada por parametro"""
      lista_nueva = []
      for i in range (len(lista)):
            for j in range (i,len(lista[i])):
                  if len(lista[i][j]) != 0:
                        lista_nueva.append(lista[i][j])
      #print(lista_nueva)
      return lista_nueva

import Modulos_y_Paquetes.Funciones_Cami as PAQ

def listar_productos_ordenado_por_nombre(lista:list):
      lista_solo_con_productos = armar_lista_con_produtos(lista)
      for i in range(len(lista)-1):
            for j in range(i+1,len(lista)):
                  if lista[i][0] > lista[j][0]:
                        PAQ.swapear_lista(lista_solo_con_productos,i,j)
      
      for i in range(len(lista_solo_con_productos)):
            print(lista_solo_con_productos[i])


#----------------------------------------------------------------------------------------
#Ejercicio ferreteria

def reponer_mercaderia(lista:list):
      """Solicita ubicacion de un producto(fila/columna)
      Si no existe prodcuto sale de la funcion
      Si existe un producto acumulara la cantidad de piezas indicada por el usuario
      a las ya existentes"""
      fila = int(input("Indique la fila donde se encuentra el producto a reponer(1-4): "))
      while fila - 1 < 0 or fila -1 > 3:
            fila = int(input("Fila no valida. Indique la fila donde se encuentra el producto a reponer(1-4): "))
      columna = int(input("Indique la columna donde se encuentra el producto a reponer(1-4): "))
      while columna - 1 < 0 or columna -1 > 3:
            columna = int(input("Columna no valida. Indique la columna donde se encuentra el producto a reponer(1-4): "))
      
      if len(lista[fila-1][columna-1]) == 0:
            print("No existe ningun producto para reponer")

      else:
            print("Usted repondra el producto", lista[fila-1][columna-1][0], 
                  "actualmente hay", lista[fila-1][columna-1][1],"piezas")
            cantidad = int(input("¿Cuantas piezas va a ingresar? "))
            lista[fila-1][columna-1][1] += cantidad

      for i in range(len(lista)):
            print(lista[i])





def vender_mercaderia(lista:list):
      """Solicita ubicacion de un producto(fila/columna)
      Si no existe prodcuto sale de la funcion
      Si existe un producto, pregunta la cantidad a vender,
      Si alcanza, modifica el stock, si no alcanzan los prodcutos existentes
      dara aviso y saldra de la funcion."""

      fila = int(input("Indique la fila donde se encuentra el producto a reponer(1-4): "))
      while fila - 1 < 0 or fila -1 > 3:
            fila = int(input("Fila no valida. Indique la fila donde se encuentra el producto a reponer(1-4): "))
      columna = int(input("Indique la columna donde se encuentra el producto a reponer(1-4): "))
      while columna - 1 < 0 or columna -1 > 3:
            columna = int(input("Columna no valida. Indique la columna donde se encuentra el producto a reponer(1-4): "))
      
      if len(lista[fila-1][columna-1]) == 0:
            print("No existe ningun producto para reponer")
      else:
            print("Usted vendera el producto", lista[fila-1][columna-1][0], 
                  "actualmente hay", lista[fila-1][columna-1][1],"piezas")
            cantidad_a_vender = int(input("¿Cuantas piezas desea vender? (0-" + str(lista[fila-1][columna-1][1])+") " ))
            while cantidad_a_vender > lista[fila-1][columna-1][1] or cantidad_a_vender < 0:
                 cantidad_a_vender = int(input("Ingreso no valido ¿Cuantas piezas desea vender? (0-"+ str(lista[fila-1][columna-1][1])+ ") ")) 
            lista[fila-1][columna-1][1] -= cantidad_a_vender

      for i in range(len(lista)):
            print(lista[i])


def listar_inventario(lista:list):
      """Recorre la lista, y la imprime """
      for i in range(len(lista)):
            for j in range(len(lista[i])):
                  print(lista[i][j], end = "    ")
      #Opcion 2
      for i in range(len(lista)):
            for j in range (len(lista[i])):
                  print(f"Del producto {lista[i][j][0]} hay {lista[i][j][1]} piezas")
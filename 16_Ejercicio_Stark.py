#Desafío Stark 
#Industrias Stark es principalmente una empresa de defensa que desarrolla y fabrica armas 
#avanzadas y tecnologías militares. 
#Recientemente ha decidido ampliar su departamento de IT y para acceder a las entrevistas es 
#necesario completar el siguiente desafío. 
#La empresa compartió con todos los participantes cierta información confidencial de un 
#grupo de superhéroes. Quien supere todo lo solicitado accederá a una entrevista con el 
#director de la compañía. 
#Set de datos 
#La información a ser analizada se encuentra en el archivo data_stark.py, por tratarse de una 
#lista, bastará con incluir dicho archivo en el proyecto de la siguiente manera: 
#from data_stark import lista_personajes 
#Formato de los datos recibidos 
lista_heroes = [ 
{ 
"nombre": "Howard the Duck", 
"identidad": "Howard (Last name unrevealed)", 
"empresa": "Marvel Comics", 
"altura": "79.349999999999994", 
"peso": "18.449999999999999", 
"genero": "M", 
"color_ojos": "Brown", 
"color_pelo": "Yellow", 
"fuerza": "2", 
"inteligencia": "average" 
}, 
{ 
"nombre": "Rocket Raccoon", 
"identidad": "Rocket Raccoon", 
"empresa": "Marvel Comics", 
"altura": "122.77", 
"peso": "25.73", 
"genero": "M", 
"color_ojos": "Brown", 
"color_pelo": "Brown", 
"fuerza": "5", 
"inteligencia": "average" 
} 
] 

#Desafío: 
#Realizar una función con el siguiente Menú de Opciones: 
#A. Listar ordenado por Nombre.  Lista todos los datos de cada superhéroe ordenados por 
#Nombre de manera ascendente. 
#B. Listar Masculinos débiles.  Recorrer la lista y determinar cuál es el superhéroe más débil de 
#género M. 
#C. Cantidad por color de ojos.  Determinar cuántos superhéroes tienen cada tipo de color de 
#ojos. 
#D. Listar por color de Pelo.  Listar todos los superhéroes agrupados por color de pelo. 
#E. Listar inteligencia.  Listar todos los superhéroes agrupados por tipo de inteligencia. 
#E. Listar Promedio.  Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier 
#género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género 
#femenino 
#F. Asignar IMC.  Calcular el índice de masa corporal de cada superhéroe y guardarla en un 
#nuevo campo.  Se deberá hacer uso de una función lambda que asignará a cada superhéroe el  
#IMC calculado. 
#Nota:   
#Crear una función para cada opción de menú. 
#Desarrollar las funciones en una biblioteca. 
#Utilizar todo lo visto en clases, métodos, funciones lambda, operadores ternarios, etc.
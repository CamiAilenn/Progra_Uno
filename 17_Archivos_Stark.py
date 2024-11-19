#Desafío Stark 
#Industrias Stark es principalmente una empresa de defensa que desarrolla y fabrica armas 
#avanzadas y tecnologías militares. 
#Recientemente ha decidido ampliar su departamento de IT y para acceder a las entrevistas es 
#necesario completar el siguiente desafío. 
#La empresa compartió con todos los participantes cierta información confidencial de un grupo 
#de superhéroes. Quien supere todo lo solicitado accederá a una entrevista con el director de la 
#compañía. 
#Set de datos 
#La información a ser analizada se encuentra en el archivo data_stark.json. 
#Desafío: 
#Funciones: 
#1.Crear la función leer_json() que va a recibir el nombre y extensión de donde se ubica el 
#archivo a leer (Ruta absoluta o relativa), y también el nombre de la lista a leer por ejemplo en la 
#imagen anterior la lista está en la clave “heroes” Si el archivo existe deberia leer el archivo json 
#y retornar la lista obtenida. 
#Si el achivo no existe deberia retornar False (USAR EXCEPCIONES) 
#2. Crear la función generar_csv() 
#La función va a recibir el nombre y extensión del archivo csv de los superhéroes (Puede ser ruta 
#absoluta o relativa) y la lista de los mismos. Si la lista no está vacía la función deberá guardar 
#en un string la información en formato csv (separado con comas) con la cabecera 
#correspondiente. 
#Una vez generado el string debería usar la función del siguiente punto (3) para guardar ese 
#string generado al archivo. Si la lista está vacía retornar False  
#Debería quedar algo como esto: 
#3. Crear la función 'guardar_archivo' la cual recibirá por parámetro un string que indicará el 
#nombre con el cual se guardará el archivo junto con su extensión (ejemplo: 'archivo.csv') y 
#como segundo parámetro tendrá un string el cual será el contenido a guardar en dicho archivo. 
#Debe abrirse el archivo en modo escritura+, ya que en caso de no existir, lo creara y en caso de 
#existir, lo va a sobreescribir La función debera retornar True si no hubo errores, caso contrario 
#False (VALIDAR CON EXCEPCIONES), además en caso de éxito, deberá imprimir un 
#mensaje respetando el formato: 
#Se creó el archivo: nombre_archivo.csv 
#ATENCIÓN: Controlar las excepciones posibles en caso de presentarse alguna retornar false e 
#imprimir un mensaje que diga: ‘Error al crear el archivo: nombre_archivo’ Donde 
#nombre_archivo será el nombre que recibirá el archivo a ser creado, conjuntamente con su 
#extensión. 
#Menú de Opciones: 
#A. Leer archivo JSON.   
#B. Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera 
#ascendente 
#C. Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario. 
#D. Salir 
#Nota:   
#Crear una función para cada opción de menú. 
#Desarrollar las funciones en una biblioteca. 
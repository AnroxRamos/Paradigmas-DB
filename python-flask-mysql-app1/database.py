import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'tilindb' #Nombre del controlador odbc para el funcionamiento de la parctica
)

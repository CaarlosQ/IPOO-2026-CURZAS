import mysql.connector
from Producto import Producto

class ConectarMysql:
    def __init__(self):
        self.connection = None
        
    def connect(self):
        try:
            print("Intentando conectar con MySQL")
            self.connection = mysql.connector.connect(
                host="localhost",
                user="carlos_quintulen",
                password="Ipoo_2026",
                database="inventario_ipoo"
            )
            if self.connection.is_connected():
                print("conexión exitosa")
        except mysql.connector.Error as e:
            print("Error al conectarse a la base de datos", e)
    
        

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            if not self.connection.is_connected():
                print("Conexión cerrada con éxito")

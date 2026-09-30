from datetime import datetime
from prestamo import Prestamo

class Biblioteca:
    def __init__(self, nombre:str):
        self.__nombre:str = nombre
        self.__coleccion_libros:list = []
        self.__coleccion_usuarios:list = []
        self.__coleccion_prestamos:list = []

    def mostrar_coleccion_libros(self):
        return self.__coleccion_libros
   
    def agregar_libro(self, nuevo_libro):
        self.__coleccion_libros.append(nuevo_libro)
    
    def mostrar_coleccion_usuarios(self):
        return self.__coleccion_usuarios

    def registrar_usuario(self, nuevo_usuario):
        self.__coleccion_usuarios.append(nuevo_usuario)

    def mostrar_coleccion_prestamos(self):
        return self.__coleccion_prestamos
  
    def agregar_prestamo(self, nuevo_prestamo):
        self.__coleccion_prestamos.append(nuevo_prestamo)
    
    def prestar_libro(self, dni, isbn):
        usuario_encontrado = self.buscar_usuario_dni(dni)
        libro_encontrado= self.buscar_libro_isbn(isbn)
        if usuario_encontrado == None:
            print("Usuario no encontrado")
        elif libro_encontrado == None:
            print("Libro no encontrado")
        else:
            libro_encontrado.prestar()
            nuevo_prestamo = Prestamo(usuario_encontrado, libro_encontrado, datetime.now())
            self.agregar_prestamo(nuevo_prestamo)
            print(f"El libro {libro_encontrado.nombre} fue prestado al usuario {usuario_encontrado.nombre} {usuario_encontrado.apellido}")

    def buscar_libro_nombre(self, nombre_libro):
        for libro in self.__coleccion_libros:
            if libro.nombre == nombre_libro:
                return libro
        return None
    def buscar_libro_isbn(self, isbn):
        for libro in self.__coleccion_libros:
            if libro.isbn == isbn:
                return libro
        return None
    def devolver_libro(self, isbn):
        libro_encontrado = self.buscar_libro_isbn(isbn)
        if libro_encontrado == None:
            print("Libro no encontrado")
        else:
            prestamo_encontrado = self.prestamo_activo(libro_encontrado)
            if prestamo_encontrado == None:
                print("Este libro no tiene un préstamo activo")
            else:
                prestamo_encontrado.devolver_prestamo()
                print("Libro devuelto con éxito")

    def mostrar_prestamo_usuario(self, dni):
        for prestamo in self.__coleccion_prestamos:
            if prestamo.consultar_usuario().dni == dni:
                print(prestamo)

    def buscar_usuario_dni(self, dni):
        for usuario in self.__coleccion_usuarios:
            if usuario.dni == dni:
                return usuario
        return None
    def prestamo_activo(self, libro):
        for prestamo in self.__coleccion_prestamos:
            if prestamo.consultar_libro() == libro and prestamo.consultar_estado_prestamo() == "Activo":
                return prestamo            
        return None

    def mostrar_prestamos(self):
        print("Prestamos activos")
        for prestamo in self.__coleccion_prestamos:
            if prestamo.consultar_estado_prestamo() == "Activo":
                print(prestamo)

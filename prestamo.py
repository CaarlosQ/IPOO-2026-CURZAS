from libro import Libro
from usuario import Usuario
class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo):
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__estado_prestamo = "Activo"

    def consultar_libro(self):
        return self.__libro

    def consultar_usuario(self):
        return self.__usuario

    def consultar_fecha_prestamo(self):
        return self.__fecha_prestamo

    def consultar_estado_prestamo(self):
        return self.__estado_prestamo

    def devolver_prestamo(self):
        if self.__estado_prestamo == "Activo":
            self.__libro.devolver()
            self.__estado_prestamo = "Devuelto"

    def __str__(self):
        return f"Usuario: {self.consultar_usuario().nombre} {self.consultar_usuario().apellido}\nLibro: {self.consultar_libro().nombre}\nFecha: {self.consultar_fecha_prestamo()}\nEstado: {self.consultar_estado_prestamo()}\n-"

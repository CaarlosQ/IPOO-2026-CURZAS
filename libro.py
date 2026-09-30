from datetime import datetime

class Libro:
    def __init__(self, isbn: str, nombre: str, autor: str, anio_publicacion: str, genero: str, cant_paginas: str):
        self.__estado_creacion_valido = False 
        
        if isbn == "" or nombre == "" or autor == "" or genero == "":
            print("Error: ISBN, Título, Autor y Género no pueden estar vacíos.")
            return

        try:
            anio_int = int(anio_publicacion)
            paginas_int = int(cant_paginas)
        except ValueError:
            print("Error: El año de publicación y la cantidad de páginas deben ser números válidos.")
            return

        anio_actual = datetime.now().year
        if paginas_int <= 0:
            print("Error: La cantidad de páginas debe ser mayor a 0.")
            return
        
        if anio_int < 0 or anio_int > anio_actual:
            print("Error: El año de publicación es inválido.")
            return

        self.__isbn: str = isbn
        self.__nombre: str = nombre
        self.__autor: str = autor
        self.__anio_publicacion: str = str(anio_int)
        self.__genero: str = genero
        self.__cant_paginas: int = paginas_int
        
        self.__disponible: bool = True
        self.__cantidad_prestamos: int = 0
        
        self.__estado_creacion_valido = True

    @property
    def creacion_valida(self) -> bool:
        return self.__estado_creacion_valido

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def autor(self) -> str:
        return self.__autor

    @property
    def anio_publicacion(self) -> str:
        return self.__anio_publicacion

    @property
    def genero(self) -> str:
        return self.__genero

    @property
    def cant_paginas(self) -> int:
        return self.__cant_paginas

    def prestar(self) -> bool:
        if self.__disponible == False:
            print(f"El libro {self.nombre} no está disponible.")
            return False
        else:
            print(f"Libro prestado: {self.nombre}.")
            self.__cantidad_prestamos += 1
            self.__disponible = False
            return True

    def devolver(self) -> bool:
        if self.__disponible == False:
            self.__disponible = True
            print(f"El libro {self.nombre} ha sido devuelto con éxito.")
            return True
        else:
            print(f"El libro {self.nombre} ya se encuentra en la lista, no puede ser devuelto.")
            return False

    def esta_disponible(self) -> bool:
        return self.__disponible

    def cantidad_prestamos(self) -> int:
        return self.__cantidad_prestamos

    def mostrar_informacion(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.nombre}") 
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio_publicacion}")
        print(f"Género: {self.genero}")
        print(f"Páginas: {self.cant_paginas}")
        print(f"Estado: {estado}")
        print(f"Préstamos: {self.__cantidad_prestamos}")
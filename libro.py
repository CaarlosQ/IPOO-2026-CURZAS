
class Libro:
    
    def __init__(self, isbn:str, nombre:str, autor:str, anio_publicacion:str, genero:str, cant_paginas:int):
        self.__isbn:str = isbn
        self.__nombre:str = nombre
        self.__autor:str = autor
        self.__anio_publicacion:str = anio_publicacion
        self.__genero:str = genero
        self.__cant_paginas:int = cant_paginas
        
        self.__disponible:bool = True
        self.__cantidad_prestamos:int = 0
    
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
            print(f"Puede llevarse el libro {self.nombre}.")
            self.__cantidad_prestamos += 1
            self.__disponible = False
            return True

    def devolver(self):
        if self.__disponible == False:
            self.__disponible = True
            print(f"El libro {self.nombre} ha sido devuelto con éxito.")
            return True
        else:
            print(f"El libro {self.nombre} ya se encuentra disponible.")
            return False

    def esta_disponible(self) -> bool:
        return self.__disponible

    def cantidad_prestamos(self) -> int:
        return self.__cantidad_prestamos

    def mostrar_informacion_libro(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.nombre}") 
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio_publicacion}")
        print(f"Género: {self.genero}")
        print(f"Páginas: {self.cant_paginas}")
        print(f"Estado: {estado}")
        print(f"Préstamos: {self.__cantidad_prestamos}")
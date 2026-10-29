from Videojuego import Videojuego
from GeneroVideojuego import GeneroVideojuego

class CatalogoVideojuegos:
    def __init__(self):
        self.__videojuegos = []

    def agregar_videojuego(self, videojuego):
        if not isinstance(videojuego, Videojuego):
            raise TypeError("El objeto no es un Videojuego")
        
        for v in self.__videojuegos:
            if v.codigo is videojuego.codigo or v.codigo == videojuego.codigo:
                return False
        
        self.__videojuegos.append(videojuego)
        return True

    def construir_y_agregar_videojuego(self, codigo, titulo, genero, precio, stock):
        for v in self.__videojuegos:
            if v.codigo is codigo or v.codigo == codigo:
                return False
        nuevo_juego = Videojuego(codigo, titulo, genero, precio, stock)
        self.__videojuegos.append(nuevo_juego)
        return True

    def mostrar_catalogo(self):
        return [v.mostrar_informacion() for v in self.__videojuegos]

    def buscar_por_codigo(self, codigo):
        for videojuego in self.__videojuegos:
            if videojuego.codigo == codigo:
                return videojuego
        return None

    def filtrar_por_genero(self, genero):
        resultado = []
        for videojuego in self.__videojuegos:
            if videojuego.genero is genero:
                resultado.append(videojuego)
        return resultado

    def mostrar_cantidad_total(self):
        return len(self.__videojuegos)

    def modificar_descuento_catalogo(self, nuevo_descuento):
        Videojuego.modificar_descuento_general(nuevo_descuento)

    def serializar(self):
        return [videojuego.serializar() for videojuego in self.__videojuegos]

    @classmethod
    def deserializar(cls, datos):
        catalogo = cls()
        for dato in datos:
            juego = Videojuego.deserializar(dato)
            catalogo.__videojuegos.append(juego)
        return catalogo
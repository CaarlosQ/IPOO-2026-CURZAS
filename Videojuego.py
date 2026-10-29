from GeneroVideojuego import GeneroVideojuego

class Videojuego:
    __contador_videojuegos = 0
    __descuento_general = 0.0

    def __init__(self, codigo, titulo, genero, precio, stock):
        if not Videojuego.validar_precio(precio):
            print("Precio inválido")
        if not Videojuego.validar_stock(stock):
            print("Stock inválido")
        if not isinstance(genero, GeneroVideojuego):
            print("Género inválido")
        
        self.__codigo = codigo
        self.__titulo = titulo
        self.__genero = genero
        self.__precio = precio
        self.__stock = stock
        Videojuego.__contador_videojuegos += 1

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def genero(self):
        return self.__genero

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def mostrar_informacion(self):
        return f"Código: {self.__codigo} | Título: {self.__titulo} | Género: {self.__genero.name} | Precio: ${self.__precio} | Stock: {self.__stock}"

    def calcular_precio_final(self):
        return self.__precio * (1 - Videojuego.__descuento_general / 100)

    @classmethod
    def modificar_descuento_general(cls, nuevo_descuento):
        cls.__descuento_general = nuevo_descuento

    @classmethod
    def obtener_cantidad_videojuegos(cls):
        return cls.__contador_videojuegos

    @staticmethod
    def validar_precio(precio):
        return isinstance(precio, (int, float)) and precio > 0

    @staticmethod
    def validar_stock(stock):
        return isinstance(stock, int) and stock >= 0

    def serializar(self):
        return {
            "codigo": self.__codigo,
            "titulo": self.__titulo,
            "genero": self.__genero.name,
            "precio": self.__precio,
            "stock": self.__stock
        }

    @classmethod
    def deserializar(cls, datos):
        genero_enum = GeneroVideojuego[datos["genero"]]
        return cls(
            datos["codigo"],
            datos["titulo"],
            genero_enum,
            datos["precio"],
            datos["stock"]
        )
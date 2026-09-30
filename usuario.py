class Usuario:
    def __init__(self, dni:str, nombre:str, apellido:str):
        self.__dni:str = dni
        self.__nombre:str = nombre
        self.__apellido:str = apellido

    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido
    @property
    def dni(self):
        return self.__dni

    def mostrar_info_usuario(self):
        return f"Nombre y Apellido: {self.__nombre} {self.__apellido}\nDNI: {self.__dni}"
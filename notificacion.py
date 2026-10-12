from abc import ABC, abstractmethod

class Notificacion(ABC):

    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje

    def mostrar_resumen(self):
        print(f"Destinatario: {self.destinatario}")
        print(f"Mensaje: {self.mensaje}")

    @abstractmethod
    def enviar(self):
        pass
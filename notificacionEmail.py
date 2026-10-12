from notificacion import Notificacion
from confirmableInterface import ConfirmableInterface


class NotificacionEmail(Notificacion, ConfirmableInterface):
    def __init__(self, destinatario, mensaje, asunto):
        super().__init__(destinatario, mensaje)
        self.asunto = asunto

    def enviar(self):
        print(f"Enviando correo: {self.mensaje}")

    def confirmar_lectura(self):
        print("Lectura confirmada.")
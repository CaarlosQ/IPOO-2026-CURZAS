from notificacion import Notificacion
from confirmableInterface import ConfirmableInterface


class NotificacionWhatsApp(Notificacion, ConfirmableInterface):
    def enviar(self):
        print(f"Enviando WhatsApp: {self.mensaje}")

    def confirmar_lectura(self):
        print("Lectura confirmada.")
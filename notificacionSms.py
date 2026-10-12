from notificacionEmail import NotificacionEmail
from confirmableInterface import ConfirmableInterface
from notificacion import Notificacion

class NotificacionSMS(Notificacion):
    def enviar(self):
        print(f"Enviando SMS: {self.mensaje}")




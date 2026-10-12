from notificacionEmail import NotificacionEmail
from notificacionSms import NotificacionSMS
from notificacionWhatsApp import NotificacionWhatsApp
from confirmableInterface import ConfirmableInterface

def main():
    notificaciones = [
        NotificacionEmail("ana@email.com", "Su inscripción fue registrada.",
                          "Inscripción"),
        NotificacionSMS("2920XXXXXX", "Su turno es a las 10:00."),
        NotificacionWhatsApp("2920YYYYYY", "Su pedido está en camino."),
    ]

    for notificacion in notificaciones:
        notificacion.mostrar_resumen()
        notificacion.enviar()

        if isinstance(notificacion, ConfirmableInterface):
            notificacion.confirmar_lectura()

        print()

if __name__ == "__main__":
    main()
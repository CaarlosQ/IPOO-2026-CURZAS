1. ¿Por qué Notificacion debería ser abstracta y no una clase común?

- Porque una notificación genérica no existe por sí sola: no se sabe cómo se envía. La clase abstracta concentra lo común (destinatario, mensaje, mostrar_resumen) y evita crear objetos incompletos, ya que no se puede instanciar directamente.

2. ¿Qué ventaja aporta obligar a todas las clases hijas a implementar enviar()?

- Todo objeto Notificacion sabrá enviarse. Así el código que usa las notificaciones puede llamar a enviar() sin saber de qué tipo es, y si una hija olvida implementarlo, Python lanza un error al intentar instanciarla.

3. ¿Por qué Confirmable no se implementa necesariamente en todos los tipos
   de notificación?

- Porque la confirmación de lectura no es una característica común a todas: el SMS no la ofrece. Al ser una interfaz separada, solo la implementan las clases que realmente tienen ese comportamiento (Email y WhatsApp), sin forzar métodos que no sirvan en las demás.

4. ¿Dónde se observa el polimorfismo en el programa principal?

- En el for que recorre la lista: se llama a mostrar_resumen() y enviar() sobre cada elemento sin importar su clase concreta, y cada objeto responde con su propia versión de enviar() (correo, SMS o WhatsApp). También al usar Confirmable como referencia común (isinstance) para llamar a confirmar_lectura().

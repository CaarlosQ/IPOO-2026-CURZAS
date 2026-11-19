# Actividad 9: Verificación de persistencia

## Procedimiento realizado

1. Ejecuté `python main.py` y, con la opción 1, se registraron dos productos.
2. Cerré la aplicación con la opción 7 (Salir).
3. La volví a ejecutar `python main.py` y se usó la opción 2 (Listar todos los productos).
4. Los dos productos seguían almacenados: aparecían con el mismo ID y los mismos datos.

## Respuestas

**a. ¿Por qué persisten los productos al finalizar el programa?**

Porque los no se guardan en la base de datos inventario_ipoo. Al ejecutar `commit()`, MySQL confirma el cambio y lo escribe en el disco. Al volver a ejecutar el programa, este se reconecta y recupera los registros con `SELECT`.

**b. ¿Qué diferencia existe entre un objeto en memoria y un registro en MySQL?**

Un objeto `Producto` vive en la memoria RAM mientras el programa está en ejecución y desaparece cuando este termina. Un registro de MySQL es una fila de la tabla `productos` guardada de forma permanente. El objeto se usa para trabajar con los datos dentro del programa, y el registro es la copia que perdura. Para pasar de uno al otro, la clase `Producto` convierte el objeto en un `INSERT` o `UPDATE`, y cada fila de un `SELECT` en un objeto `Producto`.

**c. ¿Qué función cumple `commit()`?**

Confirma de forma definitiva los cambios hechos con `INSERT`, `UPDATE` o `DELETE`. Hasta que se ejecuta, los cambios quedan en una transacción pendiente que otras conexiones no ven. Si no se llama a `commit()`, al cerrar la conexión se pierden. Si ocurre un error, `rollback()` deshace los cambios pendientes.

**d. ¿En qué se diferencian `fetchone()` y `fetchall()`?**

`fetchone()` devuelve una sola fila del resultado (la siguiente disponible), o `None` si no hay más. Se usa cuando se espera un único registro, como en `obtener_por_id`. `fetchall()` devuelve una lista con todas las filas restantes, y una lista vacía si no hay ninguna. Se usa cuando se esperan varios registros, como en `obtener_todos` y `buscar_por_categoria`.

**e. ¿Por qué se deben utilizar consultas parametrizadas?**

Porque separan el código SQL de los datos que ingresa el usuario. El conector envía los valores por separado de la sentencia (los marcadores `%s`), por lo que MySQL los trata siempre como datos y nunca como código. Así se evita la inyección SQL: por ejemplo, si alguien escribe `'; DROP TABLE productos; --` como nombre, se guarda como un texto más. Además, se manejan solos los tipos de datos y las comillas.

**f. ¿Qué sucede cuando una consulta no encuentra registros?**

No se produce ningún error: la consulta se ejecuta bien y simplemente no devuelve filas. `fetchone()` devuelve `None` y `fetchall()` devuelve una lista vacía. Por eso el programa lo controla: `obtener_por_id` informa que no existe el producto y devuelve `None`, y `buscar_por_categoria` devuelve una lista vacía, con lo que el menú muestra el mensaje "No se encontraron productos". En las modificaciones y eliminaciones, el equivalente es que `rowcount` vale 0.

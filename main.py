import math

from ConectarMysql import ConectarMysql
from Producto import Producto

PRECIO_MAXIMO = 99999999.99


def leer_texto(mensaje, maximo, obligatorio=True, valor_actual=None):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            if valor_actual is not None:
                return valor_actual
            if not obligatorio:
                return None
            print("Error: este campo no puede estar vacío.")
        elif len(texto) > maximo:
            print(f"Error: el texto no puede superar los {maximo} caracteres.")
        else:
            return texto


def leer_entero(mensaje, minimo, valor_actual=None):
    while True:
        texto = input(mensaje).strip()
        if texto == "" and valor_actual is not None:
            return valor_actual
        try:
            numero = int(texto)
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue
        if numero < minimo:
            print(f"Error: el valor debe ser mayor o igual a {minimo}.")
        else:
            return numero


def leer_precio(mensaje, valor_actual=None):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        if texto == "" and valor_actual is not None:
            return valor_actual
        try:
            precio = float(texto)
        except ValueError:
            print("Error: debe ingresar un número válido.")
            continue
        if not math.isfinite(precio) or precio <= 0:
            print("Error: el precio debe ser mayor que cero.")
        elif precio > PRECIO_MAXIMO:
            print(f"Error: el precio no puede superar {PRECIO_MAXIMO:.2f}.")
        else:
            return round(precio, 2)


def leer_id(mensaje="ID del producto: "):
    return leer_entero(mensaje, 1)


def confirmar(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Error: responda con 's' o 'n'.")


def mostrar_menu():
    print("\n===== INVENTARIO DE PRODUCTOS =====")
    print("1. Registrar producto")
    print("2. Listar todos los productos")
    print("3. Buscar producto por ID")
    print("4. Buscar productos por categoría")
    print("5. Modificar producto")
    print("6. Eliminar producto")
    print("7. Salir")


def mostrar_productos(productos):
    for producto in productos:
        print("-" * 30)
        print(producto.mostrar_info())
    print("-" * 30)


def registrar_producto(gestor):
    print("\n--- REGISTRAR PRODUCTO ---")
    nombre = leer_texto("Nombre: ", 100)
    descripcion = leer_texto("Descripción (opcional): ", 255, obligatorio=False)
    precio = leer_precio("Precio: ")
    stock = leer_entero("Stock: ", 0)
    categoria = leer_texto("Categoría: ", 50)
    gestor.insertar(Producto(None, nombre, descripcion, precio, stock, categoria))


def listar_productos(gestor):
    print("\n--- LISTADO DE PRODUCTOS ---")
    productos = gestor.obtener_todos()
    if not productos:
        print("No hay productos registrados.")
    else:
        mostrar_productos(productos)


def buscar_por_id(gestor):
    print("\n--- BUSCAR POR ID ---")
    producto = gestor.obtener_por_id(leer_id())
    if producto is not None:
        print("-" * 30)
        print(producto.mostrar_info())
        print("-" * 30)


def buscar_por_categoria(gestor):
    print("\n--- BUSCAR POR CATEGORÍA ---")
    categoria = leer_texto("Categoría: ", 50)
    productos = gestor.buscar_por_categoria(categoria)
    if not productos:
        print(f"No se encontraron productos en la categoría '{categoria}'.")
    else:
        mostrar_productos(productos)


def modificar_producto(gestor):
    print("\n--- MODIFICAR PRODUCTO ---")
    producto = gestor.obtener_por_id(leer_id())
    if producto is None:
        return
    print("-" * 30)
    print(producto.mostrar_info())
    print("-" * 30)
    print("Presione Enter para mantener el valor actual.")
    producto.set_nombre(leer_texto("Nuevo nombre: ", 100, valor_actual=producto.get_nombre()))
    nueva_descripcion = leer_texto("Nueva descripción: ", 255, obligatorio=False)
    if nueva_descripcion is not None:
        producto.set_descripcion(nueva_descripcion)
    producto.set_precio(leer_precio("Nuevo precio: ", producto.get_precio()))
    producto.set_stock(leer_entero("Nuevo stock: ", 0, producto.get_stock()))
    producto.set_categoria(leer_texto("Nueva categoría: ", 50, valor_actual=producto.get_categoria()))
    gestor.actualizar(producto)


def eliminar_producto(gestor):
    print("\n--- ELIMINAR PRODUCTO ---")
    producto = gestor.obtener_por_id(leer_id())
    if producto is None:
        return
    print("-" * 30)
    print(producto.mostrar_info())
    print("-" * 30)
    if confirmar("¿Está seguro de que desea eliminar este producto? (s/n): "):
        gestor.eliminar(producto.get_id())
    else:
        print("Eliminación cancelada.")


def menu(gestor):
    opcion = ""
    while opcion != "7":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_producto(gestor)
        elif opcion == "2":
            listar_productos(gestor)
        elif opcion == "3":
            buscar_por_id(gestor)
        elif opcion == "4":
            buscar_por_categoria(gestor)
        elif opcion == "5":
            modificar_producto(gestor)
        elif opcion == "6":
            eliminar_producto(gestor)
        elif opcion == "7":
            print("Programa finalizado.")
        else:
            print("Error: opción inválida. Elija un número del 1 al 7.")


def main():
    db = ConectarMysql()
    db.connect()
    conexion = getattr(db, "connection", None)
    if conexion is None or not conexion.is_connected():
        print("No se pudo conectar a la base de datos. Finalizando.")
        return
    try:
        gestor = Producto(conexion=conexion)
        menu(gestor)
    finally:
        db.disconnect()


if __name__ == "__main__":
    main()

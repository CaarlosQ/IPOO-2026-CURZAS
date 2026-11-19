from mysql.connector import Error


class Producto:

    COLUMNAS = "id, nombre, descripcion, precio, stock, categoria"

    def __init__(self, id: int = None, nombre: str = None, descripcion: str = None,
                 precio: float = None, stock: int = None, categoria: str = None, conexion=None):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock
        self.__categoria = categoria
        self.__conexion = conexion

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        self.__stock = stock

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_conexion(self, conexion):
        self.__conexion = conexion

    def mostrar_info(self):
        descripcion = self.__descripcion if self.__descripcion else "Sin descripción"
        return (
            f"ID: {self.__id}\n"
            f"Nombre: {self.__nombre}\n"
            f"Descripción: {descripcion}\n"
            f"Precio: ${self.__precio:.2f}\n"
            f"Stock: {self.__stock}\n"
            f"Categoría: {self.__categoria}"
        )

    def fila_a_producto(self, fila):
        return Producto(fila[0], fila[1], fila[2], float(fila[3]), fila[4], fila[5], self.__conexion)

    def existe(self, id):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute("SELECT id FROM productos WHERE id = %s", (id,))
            return cursor.fetchone() is not None
        except Error as e:
            print(f"Error al verificar el producto: {e}")
            return False
        finally:
            cursor.close()

    def insertar(self, producto):
        sql = (
            "INSERT INTO productos (nombre, descripcion, precio, stock, categoria) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        valores = (
            producto.get_nombre(),
            producto.get_descripcion(),
            producto.get_precio(),
            producto.get_stock(),
            producto.get_categoria(),
        )
        cursor = self.__conexion.cursor()
        try:
            cursor.execute(sql, valores)
            self.__conexion.commit()
            producto.set_id(cursor.lastrowid)
            print(f"Producto insertado correctamente con ID {producto.get_id()}.")
            return True
        except Error as e:
            self.__conexion.rollback()
            print(f"Error al insertar el producto: {e}")
            return False
        finally:
            cursor.close()

    def obtener_todos(self):
        sql = f"SELECT {self.COLUMNAS} FROM productos ORDER BY id"
        productos = []
        cursor = self.__conexion.cursor()
        try:
            cursor.execute(sql)
            for fila in cursor.fetchall():
                productos.append(self.fila_a_producto(fila))
        except Error as e:
            print(f"Error al consultar los productos: {e}")
        finally:
            cursor.close()
        return productos

    def obtener_por_id(self, id):
        sql = f"SELECT {self.COLUMNAS} FROM productos WHERE id = %s"
        producto = None
        cursor = self.__conexion.cursor()
        try:
            cursor.execute(sql, (id,))
            fila = cursor.fetchone()
            if fila is None:
                print(f"No existe un producto con ID {id}.")
            else:
                producto = self.fila_a_producto(fila)
        except Error as e:
            print(f"Error al consultar el producto: {e}")
        finally:
            cursor.close()
        return producto

    def actualizar(self, producto):
        sql = (
            "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, "
            "stock = %s, categoria = %s WHERE id = %s"
        )
        valores = (
            producto.get_nombre(),
            producto.get_descripcion(),
            producto.get_precio(),
            producto.get_stock(),
            producto.get_categoria(),
            producto.get_id(),
        )
        cursor = self.__conexion.cursor()
        try:
            cursor.execute(sql, valores)
            self.__conexion.commit()
            if cursor.rowcount > 0:
                print(f"Producto {producto.get_id()} actualizado correctamente.")
                return True
            if self.existe(producto.get_id()):
                print(f"El producto {producto.get_id()} no cambió: los datos son iguales a los guardados.")
                return True
            print(f"No existe un producto con ID {producto.get_id()}. No se modificó ningún registro.")
            return False
        except Error as e:
            self.__conexion.rollback()
            print(f"Error al actualizar el producto: {e}")
            return False
        finally:
            cursor.close()

    def eliminar(self, id):
        cursor = self.__conexion.cursor()
        try:
            cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
            self.__conexion.commit()
            if cursor.rowcount > 0:
                print(f"Producto {id} eliminado correctamente.")
                return True
            print(f"No existe un producto con ID {id}. No se eliminó ningún registro.")
            return False
        except Error as e:
            self.__conexion.rollback()
            print(f"Error al eliminar el producto: {e}")
            return False
        finally:
            cursor.close()

    def buscar_por_categoria(self, categoria):
        sql = f"SELECT {self.COLUMNAS} FROM productos WHERE categoria = %s ORDER BY id"
        productos = []
        cursor = self.__conexion.cursor()
        try:
            cursor.execute(sql, (categoria,))
            for fila in cursor.fetchall():
                productos.append(self.fila_a_producto(fila))
        except Error as e:
            print(f"Error al consultar por categoría: {e}")
        finally:
            cursor.close()
        return productos

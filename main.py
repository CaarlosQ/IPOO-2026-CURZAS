from biblioteca import Biblioteca
from usuario import Usuario
from libro import Libro


def cargar_libros_iniciales(biblioteca):
    biblioteca.agregar_libro(Libro("9781", "El Principito", "Antoine de Saint-Exupéry", 1943, "Novela", 96))
    biblioteca.agregar_libro(Libro("9782", "Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico", 417))
    biblioteca.agregar_libro(Libro("9783", "1984", "George Orwell", 1949, "Ciencia ficción", 328))
    biblioteca.agregar_libro(Libro("9784", "Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Novela", 863))
    biblioteca.agregar_libro(Libro("9785", "Fahrenheit 451", "Ray Bradbury", 1953, "Ciencia ficción", 256))
    biblioteca.agregar_libro(Libro("9786", "El Aleph", "Jorge Luis Borges", 1949, "Cuento", 146))
    biblioteca.agregar_libro(Libro("9787", "Dune", "Frank Herbert", 1965, "Ciencia ficción", 412))
    biblioteca.agregar_libro(Libro("9788", "Orgullo y prejuicio", "Jane Austen", 1813, "Novela", 432))
    biblioteca.agregar_libro(Libro("9789", "La invención de Morel", "Adolfo Bioy Casares", 1940, "Ciencia ficción", 120))
    biblioteca.agregar_libro(Libro("9780", "Rayuela", "Julio Cortázar", 1963, "Novela", 600))


def mostrar_menu():
    print("\n=====================")
    print("= BIBLIOTECA CURZAS =")
    print("=====================")
    print("1. Mostrar libros")
    print("2. Buscar libro por ISBN")
    print("3. Buscar libro por título")
    print("4. Mostrar libros disponibles")
    print("5. Registrar usuario")
    print("6. Buscar usuario")
    print("7. Registrar préstamo")
    print("8. Registrar devolución")
    print("9. Mostrar préstamos activos")
    print("10. Mostrar préstamos de un usuario")
    print("0. Salir")
    print()

def main():
    biblioteca = Biblioteca("Biblioteca CURZAS")
    cargar_libros_iniciales(biblioteca)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        print()
        if opcion == "1":
            print("-----------------------------------------")
            print("\n--- LIBROS DE LA BIBLIOTECA ---")
            print()
            libros = biblioteca.mostrar_coleccion_libros()
            if libros:
                for libro in libros:
                    print("=============================")
                    libro.mostrar_informacion()
                    print("=============================")
                    print()
            else:
                print("No hay libros cargados.")
            print()
            print("-----------------------------------------")
        elif opcion == "2":
            print("-----------------------------------------")
            isbn = input("Ingrese ISBN del libro: ")
            libro_encontrado = biblioteca.buscar_libro_isbn(isbn)
            if libro_encontrado:
                print("=============================================================")
                print("\nLibro encontrado:")
                libro_encontrado.mostrar_informacion()
            else:
                print("No se encontró ningún libro con ese ISBN.")
            print("=============================================================")
            print()
            print("-----------------------------------------")
        elif opcion == "3":
            print("-----------------------------------------")
            titulo = input("Ingrese el título del libro: ")
            libro_encontrado = biblioteca.buscar_libro_nombre(titulo)
            if libro_encontrado:
                print("=============================================================")
                print("\nLibro encontrado:")
                libro_encontrado.mostrar_informacion()
            else:
                print("No se encontró ningún libro con ese título.")
            print("=============================================================")
            print()
            print("-----------------------------------------")
        elif opcion == "4":
            print("-----------------------------------------")
            print("\n--- LIBROS DISPONIBLES ---")
            libros = biblioteca.mostrar_coleccion_libros()
            hay_disponibles = False
            for libro in libros:
                if libro.esta_disponible():
                    print("=============================================================")
                    print(f"- {libro.nombre}")
                    hay_disponibles = True
            if not hay_disponibles:
                print("No hay libros disponibles en este momento.")
            print("=============================================================")
            print()
            print("-----------------------------------------")

        elif opcion == "5":
            print("-----------------------------------------")
            print("\n--- REGISTRAR USUARIO ---")
            dni = input("Ingrese DNI: ")
            nombre = input("Ingrese nombre: ").capitalize()
            apellido = input("Ingrese apellido: ").capitalize()
            nuevo_usuario = Usuario(dni, nombre, apellido)
            biblioteca.registrar_usuario(nuevo_usuario)
            
            print("=============================================================")
            print(f"Usuario {nombre} {apellido} registrado con éxito.")
            print("=============================================================")
            print()
            print("-----------------------------------------")

        elif opcion == "6":
            print("-----------------------------------------")
            dni = input("Ingrese DNI del usuario: ")
            usuario_encontrado = biblioteca.buscar_usuario_dni(dni)
            if usuario_encontrado:
                print("\nUsuario encontrado:")
                print("=============================================================")
                print(usuario_encontrado.mostrar_info_usuario())
            else:
                print("No se encontró ningún usuario con ese DNI.")
            print("=============================================================")
            print()
            print("-----------------------------------------")

        elif opcion == "7":
            print("-----------------------------------------")
            print("\n### REGISTRAR PRÉSTAMO ###")
            dni = input("Ingrese DNI del usuario: ")
            isbn = input("Ingrese ISBN del libro: ")
            print()
            print("=============================================================")
            biblioteca.prestar_libro(dni, isbn)
            print("=============================================================")
            print()
            print("-----------------------------------------")

        elif opcion == "8":
            print("-----------------------------------------")
            print("\n--- REGISTRAR DEVOLUCIÓN ---")
            isbn = input("Ingrese ISBN del libro a devolver: ")
            print()
            print("=============================================================")
            biblioteca.devolver_libro(isbn)
            print("=============================================================")
            print()
            print("-----------------------------------------")

        elif opcion == "9":
            print("-----------------------------------------")
            biblioteca.mostrar_prestamos()
            print("-----------------------------------------")

        elif opcion == "10":
            print("-----------------------------------------")
            dni = input("Ingrese DNI del usuario: ")
            print()
            print("=============================================================")
            biblioteca.mostrar_prestamo_usuario(dni)
            print("=============================================================")
            print()
            print("-----------------------------------------")

        elif opcion == "0":
            print("------------------------------------------------------------")
            print("Gracias por visitar la Biblioteca del CRUZAS, Hasta Pronto!.")
            print("------------------------------------------------------------")
            break

        else:
            print("-----------------------------------------")
            print("Opción inválida. Seleccione una opción correcta.")
            print("-----------------------------------------")


if __name__ == '__main__':
    main()
from libro import Libro

def libros_disponibles():
    libros = []
    libros.append(Libro("9781", "El Principito", "Antoine de Saint-Exupéry", 1943, "Novela", 96))
    libros.append(Libro("9782", "Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico", 417))
    libros.append(Libro("9783", "1984", "George Orwell", 1949, "Ciencia ficción", 328))
    libros.append(Libro("9784", "Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Novela", 863))
    libros.append(Libro("9785", "Fahrenheit 451", "Ray Bradbury", 1953, "Ciencia ficción", 256))
    libros.append(Libro("9786", "El Aleph", "Jorge Luis Borges", 1949, "Cuento", 146))
    libros.append(Libro("9787", "Dune", "Frank Herbert", 1965, "Ciencia ficción", 412))
    libros.append(Libro("9788", "Orgullo y prejuicio", "Jane Austen", 1813, "Novela", 432))
    libros.append(Libro("9789", "La invención de Morel", "Adolfo Bioy Casares", 1940, "Ciencia ficción", 120))
    libros.append(Libro("9780", "Rayuela", "Julio Cortázar", 1963, "Novela", 600))
    return libros

def mostrar_menu():
    print("\n##### BIBLIOTECA CURZAS #######")
    print("1. Mostrar todos los libros")
    print("2. Buscar libro por ISBN")
    print("3. Buscar libros por título")
    print("4. Filtrar libros por género")
    print("5. Mostrar libros disponibles")
    print("6. Registrar préstamo")
    print("7. Registrar devolución")
    print("8. Mostrar estadísticas")
    print("9. Mostrar libro más solicitado")
    print("10. Mostrar libro más antiguo")
    print("11. Mostrar cantidad de páginas de un Libro")
    print("12. Mostrar género más representado")
    print("0. Salir")

def main():
    libros = libros_disponibles()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nLIBROS DE LA BIBLIOTECA")
            for i, libro in enumerate(libros, 1):
                print(f"{i}. {libro.nombre}")

        elif opcion == "2":
            isbn = input("Ingrese ISBN: ")
            encontrado = False
            for libro in libros:
                if libro.isbn == isbn:
                    print("\nLibro encontrado:")
                    libro.mostrar_informacion_libro()
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró ningún libro con ese ISBN.")

        elif opcion == "3":
            fragmento = input("Ingrese una palabra: ").lower()
            encontrado = False
            for libro in libros:
                if fragmento in libro.nombre.lower():
                    print(f"\nSe encontro conincidencia \n- {libro.nombre}")
                    encontrado = True
            if not encontrado:
                print("No se encontró el libro")

        elif opcion == "4":
            genero = input("Ingrese género: ").lower()
            encontrado = False
            for libro in libros:
                if libro.genero.lower() == genero:
                    print(f"- {libro.nombre}")
                    encontrado = True
            if not encontrado:
                print("No hay libros regustrados que pertenezcan a ese género.")

        elif opcion == "5":
            print("\nLIBROS DISPONIBLES")
            for libro in libros:
                if libro.esta_disponible():
                    print(f"- {libro.nombre}")

        elif opcion == "6":
            isbn = input("Ingrese ISBN del libro a prestar: ")
            for libro in libros:
                if libro.isbn == isbn:
                    libro.prestar()
                    break
            else:
                print("El libro no existe o ISBN no coincide con ningún libro")

        elif opcion == "7":
            isbn = input("Ingrese ISBN del libro que va devolver: ")
            for libro in libros:
                if libro.isbn == isbn:
                    libro.devolver()
                    break
            else:
                print("ISBN de libro no válido")

        elif opcion == "8":
            total = len(libros)
            disponibles = 0
            for libro in libros:
                if libro.esta_disponible(): disponibles += 1
            prestados = total - disponibles
            print("\nESTADÍSTICAS DE LA BIBLIOTECA")
            print(f"Cantidad total de libros: {total}")
            print(f"Libros disponibles: {disponibles}")
            print(f"Libros prestados: {prestados}")
            print(f"Porcentaje disponibles: {(disponibles/total)*100}%")
            print(f"Porcentaje prestados: {(prestados/total)*100}%")

        elif opcion == "9":
            if not libros: continue
            mas_solicitado = libros[0]
            for libro in libros:
                if libro.cantidad_prestamos() > mas_solicitado.cantidad_prestamos():
                    mas_solicitado = libro
            print("\nLIBRO MÁS SOLICITADO")
            print(f"Título: {mas_solicitado.nombre}")
            print(f"Cantidad de préstamos: {mas_solicitado.cantidad_prestamos()}")

        elif opcion == "10":
            if not libros: continue
            mas_antiguo = libros[0]
            for libro in libros:
                if libro.anio_publicacion < mas_antiguo.anio_publicacion:
                    mas_antiguo = libro
            print("\nLIBRO MÁS ANTIGUO")
            print(f"Título: {mas_antiguo.nombre}")
            print(f"Año: {mas_antiguo.anio_publicacion}")

        elif opcion == "11":
            busqueda = input("Ingrese el ISBN o nombre del libro: ").lower()
            encontrado = False
            for libro in libros:
                if libro.isbn == busqueda or busqueda in libro.nombre.lower():
                    print(f"\nEl libro '{libro.nombre}' tiene {libro.cant_paginas} páginas.")
                    encontrado = True
            
            if not encontrado:
                print("No se encontró ningún libro con ese ISBN o nombre.")

        elif opcion == "12":
            generos = []
            cantidad = []
            for libro in libros:
                if libro.genero in generos:
                    indice = generos.index(libro.genero)
                    cantidad[indice] += 1
                else:
                    generos.append(libro.genero)
                    cantidad.append(1)
            
            num_conteo = 0
            genero_con_mas_apariciones = ""
            for i in range(len(generos)):
                if cantidad[i] > num_conteo:
                    num_conteo = cantidad[i]
                    genero_con_mas_apariciones = generos[i]
            
            print("\nGÉNERO MÁS REPRESENTADO")
            print(f"{genero_con_mas_apariciones}: {num_conteo} libros")

        elif opcion == "0":
            break
        else:
            print("Opción inválida, Seleccione una opción correcta.")

if __name__ == '__main__':
    main()
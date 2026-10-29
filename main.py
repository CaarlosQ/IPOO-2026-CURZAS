import json
from GeneroVideojuego import GeneroVideojuego
from Videojuego import Videojuego
from CatalogoVideojuego import CatalogoVideojuegos

def menu():
    catalogo = CatalogoVideojuegos()
    juego1 = Videojuego(codigo="1", titulo="Super Mario Bros", genero=GeneroVideojuego.AVENTURA, precio=25.2, stock=12)
    catalogo.agregar_videojuego(juego1)
    while True:
        print("\n===== CATÁLOGO DE VIDEOJUEGOS =====")
        print("1. Registrar videojuego")
        print("2. Mostrar videojuegos")
        print("3. Buscar videojuego por código")
        print("4. Filtrar videojuegos por género")
        print("5. Modificar descuento general")
        print("6. Mostrar cantidad de videojuegos")
        print("7. Guardar catálogo en archivo")
        print("8. Cargar catálogo desde archivo")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            codigo = input("Ingrese código: ")
            titulo = input("Ingrese título: ")
            print("Géneros disponibles:")
            for g in GeneroVideojuego:
                print(f"- {g.name}")
            gen_str = input("Ingrese género: ").upper()
            try:
                genero = GeneroVideojuego[gen_str]
                precio = float(input("Ingrese precio: "))
                stock = int(input("Ingrese stock: "))
                
                if catalogo.construir_y_agregar_videojuego(codigo, titulo, genero, precio, stock):
                    print("Videojuego registrado exitosamente.")
                else:
                    print("Error: Ya existe un videojuego con ese código.")
            except Exception as e:
                print(f"Error en los datos ingresados: {e}")
                
        elif opcion == "2":
            juegos = catalogo.mostrar_catalogo()
            if not juegos:
                print("El catálogo está vacío.")
            else:
                for j in juegos:
                    print(j)
                    
        elif opcion == "3":
            codigo = input("Ingrese código a buscar: ")
            juego = catalogo.buscar_por_codigo(codigo)
            if juego is not None:
                print(juego.mostrar_informacion())
                print(f"Precio final con descuento: ${juego.calcular_precio_final()}")
            else:
                print("Videojuego no encontrado.")
                
        elif opcion == "4":
            print("Géneros disponibles:")
            for g in GeneroVideojuego:
                print(f"- {g.name}")
            gen_str = input("Ingrese género a filtrar: ").upper()
            try:
                genero = GeneroVideojuego[gen_str]
                juegos = catalogo.filtrar_por_genero(genero)
                if not juegos:
                    print("No hay videojuegos para ese género.")
                else:
                    for j in juegos:
                        print(j.mostrar_informacion())
            except Exception as e:
                print(f"Género inválido: {e}")
                    
        elif opcion == "5":
            try:
                nuevo_desc = float(input("Ingrese el porcentaje de descuento general: "))
                Videojuego.modificar_descuento_general(nuevo_desc)
                print("Descuento actualizado correctamente.")
            except ValueError:
                print("Valor inválido.")
                
        elif opcion == "6":
            print(f"Cantidad total en catálogo: {catalogo.mostrar_cantidad_total()}")
            print(f"Cantidad total registrada global: {Videojuego.obtener_cantidad_videojuegos()}")
            
        elif opcion == "7":
            try:
                datos = catalogo.serializar()
                with open("catalogo.json", "w", encoding="utf-8") as archivo:
                    json.dump(datos, archivo)
                print("Catálogo guardado exitosamente.")
            except Exception as e:
                print(f"Error al guardar: {e}")
                
        elif opcion == "8":
            try:
                with open("catalogo.json", "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
                    catalogo = CatalogoVideojuegos.deserializar(datos)
                print("Catálogo cargado exitosamente.")
            except FileNotFoundError:
                print("Archivo no encontrado.")
            except Exception as e:
                print(f"Error al cargar: {e}")
                
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
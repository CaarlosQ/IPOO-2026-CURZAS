● Nombre y Apellido: Carlos Quintulen

● descripción del problema: Una biblioteca necesita un sistema de software paraadministrar su catálogo de libros. El objetivo es crear el programa teniendo en cuenta atributos y metodos de la POO para resolverlo

● descripción de la clase desarrollada: Cree la clase `Libro`.

- Atributos: `isbn`, `nombre`, `autor`, `anio_publicacion`, `genero` y `cant_paginas`
- Atributos inicializados: `__disponible` y `__cantidad_prestamos`.
- Métodos: `prestar()`, `devolver()`, `esta_disponible()` y `mostrar_informacion()`.

● explicación de cómo se aplicó la abstracción: En este caso, un libro físico tiene atributos como tamaño, peso, color. Sin embargo, para el sistema de la biblioteca, esa información es innecesaria, entonces la abstracción entra en seleccionar los datos necesarios para que la biblioteca funcione (ISBN, autor, año, género, disponibilidad, etc.), cosa que permitira poder buscar, filtrar y prestar los libros.

● explicación de cómo se aplicó el encapsulamiento: El encapsulamiento se aplicó ocultando el estado de los atributos de la clase, de modo privado con dobles guines bajos (`__`). Esto para que la información no pueda ser modificada de manera más fácil desde afuera.
Además, los decoradores los use `@property` para permitir la lectura de los atributos para mostrarle la información al ususario.
  
● descripción de los principales algoritmos implementados:
  - **Búsqueda y filtrado:** se iteró sobre toda la colección comparando una condición por cada elemento.
  - **Cálculo de extremos (Libro más solicitado / más antiguo):** Se utilizó un algoritmo que inicializa una variable para guardar el máximo o mínimo asumiendo como referencia el primer objeto de la lista y se recorre el resto. Si el objeto actual supera la condición pasa a ser la nueva referencia máxima.
  - **Promedios y estadísticas:** Algoritmos acumuladores que recorren la lista sumando el total de un valor, y al finalizar el bucle se calculan los porcentajes y promedios sobre la longitud total de la lista.

● respuestas a las preguntas conceptuales.

5. Desarrolle un programa que permita generar un reporte de estadística de las notas que se reciben en un txt. Imagine que la estructura del txt es la siguiente:
Christiane Endler;6.5
Juan Perez;5.0
Alexis Sanchez;5.5
…
Se pide que el programa lea este archivo y entregue un reporte que muestre la siguiente información:
a. Total y porcentaje de aprobados y reprobados.
b. Total y porcentaje de notas entre los rangos: 1.0-1.9, 2.0-2.9, 3.0-3.9, 4.0-4.9, 5.0-5.9, 6.0-7.0
c. Lista de alumnos en el cuartil 1, cuartil 2, cuartil 3 y cuartil 4.
Sugerencias:
Desarrolle su programa utilizando los siguientes elementos:
1. Manejo de archivos. Se recomienda manejar: open(), readlines(), write(), writelines(), close().
2. Slicing. En esta parte, tenga cuidado con el salto de línea que se importará cuando se importe la nota. Puede utilizar el método index para identificarlo, o bien, como ya se sabe que la nota siempre será de 3 caracteres, puede utilizar distintos métodos para importar bien. Recuerde que el readlines() entrega los elementos como string, pero la nota se debe trabajar como float.
3. Note que cada letra de la pregunta es una característica solicitada del sistema. Se recomienda que identifique las que más maneja y trabajar sobre ellas. Si no funciona al correr el programa, se recomienda dejar clara la lógica que se desea implementar, puesto que la asignación del puntaje es gradual, no dicotómica.
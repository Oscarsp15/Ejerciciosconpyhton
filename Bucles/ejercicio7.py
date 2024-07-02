#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# aqui sufrí :p, tuve que revisar las tablas para lograr multiplicar, pero así se aprende. 
for i in range(1, 11):
    # Mostrar el encabezado de la tabla para cada multiplicador
    print(f"Tabla del {i}:")
    # Iterar sobre los números del 1 al 10 y mostrar los productos
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    # Agregar un salto de línea entre cada tabla para mejorar la legibilidad
    print()

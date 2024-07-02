#Escribir un programa que almacene las matrices
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, 
# representando cada vector fila en una lista.


# Definir las matrices como listas anidadas
matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [-1, 0],
    [1, 1],
    [0, 1]
]

# Función para calcular el producto de dos matrices
def producto_matrices(mat1, mat2):
    # Dimensiones de las matrices
    filas_mat1 = len(mat1)
    columnas_mat1 = len(mat1[0])
    filas_mat2 = len(mat2)
    columnas_mat2 = len(mat2[0])
    
    # Verificar si las matrices se pueden multiplicar
    if columnas_mat1 != filas_mat2:
        raise ValueError("Las dimensiones de las matrices no permiten la multiplicación.")
    
    # Crear una matriz resultado inicializada con ceros
    resultado = [[0 for _ in range(columnas_mat2)] for _ in range(filas_mat1)]
    
    # Calcular el producto de las matrices
    for i in range(filas_mat1):
        for j in range(columnas_mat2):
            for k in range(filas_mat2):
                resultado[i][j] += mat1[i][k] * mat2[k][j]
    
    return resultado

# Calcular el producto de las matrices y mostrar por pantalla el resultado
try:
    resultado_producto = producto_matrices(matriz1, matriz2)
    print("El resultado del producto de las matrices es:")
    for fila in resultado_producto:
        print(fila)
except ValueError as e:
    print(e)

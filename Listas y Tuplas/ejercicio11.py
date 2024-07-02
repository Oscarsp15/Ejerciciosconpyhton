#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas 
# y muestre por pantalla su producto escalar.

# Definir los vectores como listas
vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

# Inicializar una variable para almacenar el producto escalar
producto_escalar = 0

# Calcular el producto escalar
for i in range(len(vector1)):
    producto_escalar += vector1[i] * vector2[i]

# Mostrar por pantalla el producto escalar
print(f"El producto escalar de los vectores {vector1} y {vector2} es: {producto_escalar}")

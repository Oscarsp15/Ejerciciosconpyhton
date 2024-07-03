#Escribir una función que reciba otra función y una lista, 
#y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

# Función que aplica otra función a cada elemento de una lista y devuelve los resultados en una nueva lista
def aplicar_funcion_a_lista(funcion, lista):
    resultados = []
    for elemento in lista:
        resultado = funcion(elemento)
        resultados.append(resultado)
    return resultados

# Ejemplos de funciones que podrían ser pasadas como argumento
def cuadrado(x):
    return x ** 2

def doble(x):
    return 2 * x

def inverso(x):
    return 1 / x

# Lista de prueba
numeros = [1, 2, 3, 4, 5]

# Ejemplo de uso aplicando la función cuadrado a la lista de números
resultados_cuadrado = aplicar_funcion_a_lista(cuadrado, numeros)
print("Resultados al aplicar la función cuadrado a la lista:", resultados_cuadrado)

# Ejemplo de uso aplicando la función doble a la lista de números
resultados_doble = aplicar_funcion_a_lista(doble, numeros)
print("Resultados al aplicar la función doble a la lista:", resultados_doble)

# Ejemplo de uso aplicando la función inverso a la lista de números
resultados_inverso = aplicar_funcion_a_lista(inverso, numeros)
print("Resultados al aplicar la función inverso a la lista:", resultados_inverso)




#Escribir una función que calcule el módulo de un vector.

import math

# Función para calcular el módulo de un vector
def modulo_vector(vector):
    suma_cuadrados = sum(componente ** 2 for componente in vector)
    modulo = math.sqrt(suma_cuadrados)
    return modulo

# Ejemplo de uso
vector_ejemplo = [3, 4]
modulo = modulo_vector(vector_ejemplo)
print(f"El módulo del vector {vector_ejemplo} es: {modulo}")

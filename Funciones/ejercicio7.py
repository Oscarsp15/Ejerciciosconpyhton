#Escribir una función que reciba una muestra de números en una lista 
# y devuelva otra lista con sus cuadrados.

# Función para calcular los cuadrados de una lista de números
def calcular_cuadrados(numeros):
    cuadrados = [numero ** 2 for numero in numeros]
    return cuadrados

# Usando la función
muestra = [1, 2, 3, 4, 5]
cuadrados = calcular_cuadrados(muestra)
print(f"Los cuadrados de la muestra {muestra} son {cuadrados}")

#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# Pedir al usuario los números ganadores de la lotería primitiva
print("Introduce los números ganadores de la lotería primitiva (separados por espacios):")
entrada = input()

# Convertir la entrada en una lista de números enteros
numeros = [int(numero) for numero in entrada.split()]

# Ordenar la lista de números de menor a mayor
numeros.sort()

# Mostrar los números ordenados por pantalla
print("Números ganadores de la lotería primitiva (ordenados de menor a mayor):")
for numero in numeros:
    print(numero, end=" ")
print()  # Imprimir una línea en blanco al final

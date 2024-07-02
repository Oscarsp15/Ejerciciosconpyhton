#Escribir un programa que pregunte por una muestra de números, 
# separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

import math # importo el modulo math

# Pedir al usuario una muestra de números separados por comas
entrada = input("Ingrese una muestra de números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = [float(numero.strip()) for numero in entrada.split(',')]

# Calcular la media
media = sum(numeros) / len(numeros)

# Calcular la desviación típica
suma_cuadrados = sum((x - media) ** 2 for x in numeros)
desviacion_tipica = math.sqrt(suma_cuadrados / len(numeros))

# Mostrar por pantalla la media y la desviación típica
print(f"La media de la muestra es: {media}")
print(f"La desviación típica de la muestra es: {desviacion_tipica}")




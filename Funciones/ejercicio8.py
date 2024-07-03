#Escribir una función que reciba una muestra de números en una lista 
# y devuelva un diccionario con su media, varianza y desviación típica.

import math

# Función para calcular la media de una lista de números
def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Función para calcular la varianza de una lista de números
def calcular_varianza(numeros, media):
    if len(numeros) == 0:
        return 0
    suma_diferencias_cuadradas = sum((x - media) ** 2 for x in numeros)
    return suma_diferencias_cuadradas / len(numeros)

# Función para calcular la desviación típica de una lista de números
def calcular_desviacion_tipica(varianza):
    return math.sqrt(varianza)

# Función principal para calcular media, varianza y desviación típica
def estadisticas_muestra(numeros):
    media = calcular_media(numeros)
    varianza = calcular_varianza(numeros, media)
    desviacion_tipica = calcular_desviacion_tipica(varianza)
    return {
        'media': media,
        'varianza': varianza,
        'desviacion_tipica': desviacion_tipica
    }

# Usando la función
muestra = [10, 20, 30, 40, 50]
estadisticas = estadisticas_muestra(muestra)
print(f"Las estadísticas de la muestra {muestra} son: {estadisticas}")

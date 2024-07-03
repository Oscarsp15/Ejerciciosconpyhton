#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

# Función para calcular la media de una lista de números
def calcular_media(numeros):
    if len(numeros) == 0:
        return 0  # Manejo del caso en que la lista esté vacía
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    return media

# Usando la función
muestra = [10, 20, 30, 40, 50]
media = calcular_media(muestra)
print(f"La media de la muestra {muestra} es {media}")

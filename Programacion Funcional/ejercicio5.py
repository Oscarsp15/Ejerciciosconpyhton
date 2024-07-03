#Escribir una función que reciba una frase 
# y devuelva un diccionario con las palabras que contiene y su longitud.

# Función que devuelve un diccionario con las palabras de una frase y su longitud
def longitud_palabras(frase):
    # Dividir la frase en palabras utilizando split()
    palabras = frase.split()
    
    # Crear un diccionario para almacenar las palabras y sus longitudes
    palabras_longitudes = {}
    
    # Iterar sobre cada palabra y añadir al diccionario
    for palabra in palabras:
        palabras_longitudes[palabra] = len(palabra)
    
    return palabras_longitudes

# Ejemplo de uso
frase_ejemplo = "Pablito clavó un clavito en la calva de un calvito. Un clavito clavó Pablito en la calva de un calvito. ¿Qué clavito clavó Pablito?"
resultado = longitud_palabras(frase_ejemplo)
print("Diccionario de palabras y longitudes:")
for palabra, longitud in resultado.items():
    print(f"{palabra}: {longitud}")




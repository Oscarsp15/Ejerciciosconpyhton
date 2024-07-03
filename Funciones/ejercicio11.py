#Escribir un programa que reciba una cadena de caracteres 
#y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
#Escribir otra función que reciba el diccionario generado con la función anterior 
#y devuelva una tupla con la palabra más repetida y su frecuencia.

# Función para contar la frecuencia de las palabras en una cadena de caracteres
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia_palabras = {}
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para contar de manera insensible a mayúsculas
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    return frecuencia_palabras

# Función para encontrar la palabra más repetida y su frecuencia
def palabra_mas_repetida(frecuencia_palabras):
    palabra_frecuencia_max = max(frecuencia_palabras.items(), key=lambda item: item[1])
    return palabra_frecuencia_max

# Usando las funciones
cadena = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."

frecuencia_palabras = contar_palabras(cadena)
palabra_frecuencia_max = palabra_mas_repetida(frecuencia_palabras)

print(f"Frecuencia de palabras: {frecuencia_palabras}")
print(f"La palabra más repetida es '{palabra_frecuencia_max[0]}' con una frecuencia de {palabra_frecuencia_max[1]}")

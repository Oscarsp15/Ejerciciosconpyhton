#Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
# y cada par <palabra>:<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. 
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.



diccionario = {}

# Pedir al usuario que ingrese las palabras y sus traducciones
entradas = input("Ingrese las palabras en español e inglés separadas por dos puntos (:) y cada par separado por comas (ej. casa:house,perro:dog): ")

# Dividir las entradas en pares <palabra>:<traducción> y crear el diccionario
parejas = entradas.split(',')
for pareja in parejas:
    if ':' in pareja:
        clave, valor = pareja.split(':')
        diccionario[clave.strip()] = valor.strip()

# Pedir al usuario una frase en español para traducir
frase = input("Ingrese una frase en español para traducirla: ")

# Traducir la frase palabra por palabra usando el diccionario
palabras = frase.split()
traduccion = []
for palabra in palabras:
    traduccion.append(diccionario.get(palabra, palabra))  # Si la palabra no está en el diccionario, se deja sin traducir

# Mostrar la traducción de la frase
frase_traducida = ' '.join(traduccion)
print(f"La frase traducida es: {frase_traducida}")

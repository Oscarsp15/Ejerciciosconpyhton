#Escribir un programa en el que se pregunte al usuario por una frase 
# y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Introduce una frase: ")

# Pedir al usuario que introduzca una letra
letra = input("Introduce una letra para contar en la frase: ")

# Inicializar el contador de ocurrencias de la letra
contador = 0

# Recorrer cada caracter de la frase
for caracter in frase:
    # Comparar el caracter con la letra buscada (ignorar mayúsculas y minúsculas)
    if caracter.lower() == letra.lower():
        contador += 1

# Mostrar el número de veces que aparece la letra en la frase
print(f"La letra '{letra}' aparece {contador} veces en la frase '{frase}'.")

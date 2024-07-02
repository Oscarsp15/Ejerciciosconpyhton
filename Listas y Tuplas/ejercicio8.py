#Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla si es un palíndromo.

# Pedir al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Convertir la palabra a minúsculas para ignorar diferencias de mayúsculas y minúsculas
palabra = palabra.lower()

# Verificar si la palabra es un palíndromo
if palabra == palabra[::-1]:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

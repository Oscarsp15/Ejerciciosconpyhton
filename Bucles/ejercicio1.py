#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# Pedir al usuario una palabra
palabra = input("Introduce una palabra: ")

# Mostrar la palabra por pantalla 10 veces
for _ in range(10): # uso _ por que no se necesita variable en la iteración.
    print(palabra)

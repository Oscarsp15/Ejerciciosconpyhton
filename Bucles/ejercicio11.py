#Escribir un programa que pida al usuario una palabra 
# y luego muestre por pantalla una a una las letras 
# de la palabra introducida empezando por la última.

palabra = input("Introduce una palabra: ")

# Mostrar las letras de la palabra empezando por la última
print("Las letras de la palabra empezando por la última son:")
for i in range(len(palabra) - 1, -1, -1):
    print(palabra[i])

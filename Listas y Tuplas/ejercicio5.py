#Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.


numeros = list(range(1, 11))

# Mostrar los números en orden inverso separados por comas
numeros_inverso = ", ".join(map(str, reversed(numeros)))
print(f"Números del 10 al 1 en orden inverso: {numeros_inverso}")

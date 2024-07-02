#Escribir un programa que pida al usuario dos números 
# y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

# Pedir al usuario dos números
numerador = int(input("Introduce el numerador: \n"))
divisor = int(input("Introduce el divisor: \n"))

# Verificar si el divisor es cero y realizar la división si no lo es
if divisor == 0:
    print("Error: el divisor no puede ser cero.")
else:
    resultado = numerador / divisor
    print(f"La división de {numerador} entre {divisor} es {resultado}.")

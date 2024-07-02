#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

# Pedir al usuario un número entero
numero = int(input("Introduce un número entero: \n"))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

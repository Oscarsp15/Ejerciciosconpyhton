#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# Preguntar al usuario su edad
edad = int(input("Por favor, introduce tu edad: \n"))

# Verificar si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")

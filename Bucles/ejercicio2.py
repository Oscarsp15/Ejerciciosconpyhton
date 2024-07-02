#Escribir un programa que pregunte al usuario su edad 
# y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# Edad del usuario.
edad = int(input("Por favor, introduce tu edad: "))

# Mostrar por pantalla los años cumplidos
print("Años que has cumplido:")
for i in range(1, edad + 1):
    print(i)

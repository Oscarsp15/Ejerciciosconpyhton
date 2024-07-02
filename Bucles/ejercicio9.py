#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# Almacenar la contraseña correcta en una variable
contraseña_correcta = "password123"

# Pedir al usuario que introduzca la contraseña
contraseña = input("Introduce la contraseña: ")

# Verificar si la contraseña es correcta
while contraseña != contraseña_correcta:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    contraseña = input("Introduce la contraseña: ")

# Si la contraseña es correcta, mostrar un mensaje de éxito
print("Contraseña correcta. Acceso concedido.")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
#introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# Almacenar la cadena de caracteres contraseña en una variable
contraseña_guardada = "Password123"

contraseña_usuario = input("Introduce tu contraseña: \n")

# Verificar si la contraseña introducida coincide con la guardada (ignorando mayúsculas y minúsculas)
if contraseña_usuario.lower() == contraseña_guardada.lower():
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")

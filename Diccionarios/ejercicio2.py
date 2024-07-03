#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> 
# y su número de teléfono es <teléfono>.

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")

# Crear un diccionario con la información
datos_usuario = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}

# Mostrar la información por pantalla
mensaje = f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['direccion']} y su número de teléfono es {datos_usuario['telefono']}."
print(mensaje)

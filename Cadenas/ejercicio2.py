#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla 
# el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
# otra con todas las letras mayúsculas y otra solo con la primera 
# letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre = input("introduce tu nombre: \n")

print("nombre en minuscula", nombre.lower())
print("nombre en minuscula", nombre.upper())
print("nombre en minuscula", nombre.capitalize())
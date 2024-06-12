#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, 
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# escribir un programa que pregunte por un número de teléfono con este formato 
# y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

tlf = input("Ingresa el numero de telefono de la empresa: \n")
print(f"El telefono es: {tlf[4:13]} ")


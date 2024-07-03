#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

# Crear un diccionario vacío
persona = {}

# Solicitar información y llenar el diccionario
while True:
    clave = input("Ingrese el tipo de información (nombre, edad, sexo, teléfono, correo electrónico) o 'fin' para terminar: ")

    if clave.lower() == 'fin':
        break
    
    if clave.lower() in ['nombre', 'edad', 'sexo', 'teléfono', 'correo electrónico']:
        valor = input(f"Ingrese el valor de '{clave}': ")
        persona[clave] = valor
        
        # Mostrar el contenido actual del diccionario
        print("\nContenido actual del diccionario:")
        for key, value in persona.items():
            print(f"{key}: {value}")
        print()
    else:
        print("Clave no válida. Por favor, ingrese una clave válida o 'fin' para terminar.")

# Mostrar el diccionario completo al final
print("\nDiccionario completo:")
print(persona)

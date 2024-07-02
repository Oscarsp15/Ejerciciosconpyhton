#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


numero = int(input("Introduce un número entero positivo: "))

# Validar que el número ingresado sea positivo
if numero <= 0:
    print("El número ingresado no es válido. Debe ser un entero positivo.")
else:
    # Inicializar una lista para almacenar los números impares
    impares = []

    # Iterar desde 1 hasta el número ingresado (inclusive)
    for i in range(1, numero + 1):
        # Verificar si el número es impar (resto de la división por 2 es distinto de 0)
        if i % 2 != 0:
            impares.append(i)  # Agregar el número impar a la lista

    # Convertir la lista de números impares a una cadena separada por comas
    impares_str = ", ".join(map(str, impares)) 

    # Mostrar los números impares por pantalla
    print(f"Números impares desde 1 hasta {numero}: {impares_str}")

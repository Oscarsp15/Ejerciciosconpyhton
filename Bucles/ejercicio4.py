#Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Introduce un número entero positivo: "))

# Validar que el número ingresado sea positivo
if numero <= 0:
    print("El número ingresado no es válido. Debe ser un entero positivo.")
else:
    # Inicializar una lista para almacenar los números en la cuenta atrás
    cuenta_atras = []

    # Iterar desde el número ingresado hasta 0 (inclusive), en orden descendente
    for i in range(numero, -1, -1):
        cuenta_atras.append(i)  # Agregar el número a la lista

    # Convertir la lista de números a una cadena separada por comas
    cuenta_atras_str = ", ".join(map(str, cuenta_atras))

    # Mostrar la cuenta atrás por pantalla
    print(f"Cuenta atrás desde {numero} hasta 0: {cuenta_atras_str}")



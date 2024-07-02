#Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es un número primo o no.

# Pedir al usuario un número entero
numero = int(input("Introduce un número entero positivo mayor que 1: "))

# Verificar si el número es primo
if numero > 1:
    es_primo = True  # Suponemos que el número es primo inicialmente
    # Comprobar si hay algún divisor además de 1 y el propio número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    # Mostrar el resultado
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
else:
    print("El número ingresado no es válido. Debe ser un entero positivo mayor que 1.")

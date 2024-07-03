#Escribir una función que simule una calculadora científica 
# que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. 
# La función preguntará al usuario el valor y la función a aplicar, 
# y mostrará por pantalla una tabla con los enteros de 1 al valor introducido 
# y el resultado de aplicar la función a esos enteros.

import math

# Función para simular una calculadora científica
def calculadora_cientifica():
    # Pedir al usuario el valor máximo y la función a aplicar
    valor_maximo = int(input("Introduce el valor máximo (entero positivo): "))
    funcion = input("Introduce la función a aplicar (seno, coseno, tangente, exponencial, logaritmo): ")

    # Validar la función ingresada por el usuario
    if funcion not in ['seno', 'coseno', 'tangente', 'exponencial', 'logaritmo']:
        print("Función no válida.")
        return

    # Imprimir encabezado de la tabla
    print(f"{'Entero':<10} {'Resultado'}")
    print("-" * 25)

    # Iterar sobre los enteros del 1 al valor máximo y calcular la función correspondiente
    for i in range(1, valor_maximo + 1):
        if funcion == 'seno':
            resultado = math.sin(i)
        elif funcion == 'coseno':
            resultado = math.cos(i)
        elif funcion == 'tangente':
            resultado = math.tan(i)
        elif funcion == 'exponencial':
            resultado = math.exp(i)
        elif funcion == 'logaritmo':
            resultado = math.log(i)

        # Imprimir cada fila de la tabla
        print(f"{i:<10} {resultado:.6f}")

# Ejecutar la función de la calculadora científica
calculadora_cientifica()



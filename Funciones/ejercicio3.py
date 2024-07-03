#Escribir una función que reciba un número entero positivo 
# y devuelva su factorial.

# creando función
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# usando la función
print(factorial(3))

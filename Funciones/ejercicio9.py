#Escribir una función que calcule el máximo común divisor de dos números 
# y otra que calcule el mínimo común múltiplo.

# Función para calcular el MCD usando el algoritmo de Euclides
def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para calcular el MCM usando el MCD
def calcular_mcm(a, b):
    mcd = calcular_mcd(a, b)
    return abs(a * b) // mcd

# Usando las funciones
numero1 = 48
numero2 = 18

mcd = calcular_mcd(numero1, numero2)
mcm = calcular_mcm(numero1, numero2)

print(f"El MCD de {numero1} y {numero2} es {mcd}")
print(f"El MCM de {numero1} y {numero2} es {mcm}")

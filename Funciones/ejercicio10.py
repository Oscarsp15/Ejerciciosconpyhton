#Escribir una función que convierta un número decimal en binario 
# y otra que convierta un número binario en decimal.

# Función para convertir un número decimal en binario
def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

# Función para convertir un número binario en decimal
def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in reversed(binario):
        if digito == '1':
            decimal += 2 ** potencia
        potencia += 1
    return decimal

# Usando las funciones
numero_decimal = 25
numero_binario = "11001"

binario_convertido = decimal_a_binario(numero_decimal)
decimal_convertido = binario_a_decimal(numero_binario)

print(f"El número decimal {numero_decimal} en binario es {binario_convertido}")
print(f"El número binario {numero_binario} en decimal es {decimal_convertido}")

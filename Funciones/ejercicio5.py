#Escribir una función que calcule el área de un círculo 
# y otra que calcule el volumen de un cilindro usando la primera función.

import math #importo el modulo math

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Función para calcular el volumen de un cilindro usando la primera función
def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen

# Usando las funciones
radio = 5
altura = 10

area_circulo = calcular_area_circulo(radio)
volumen_cilindro = calcular_volumen_cilindro(radio, altura)

print(f"El área del círculo con radio {radio} es {area_circulo:.2f}")
print(f"El volumen del cilindro con radio {radio} y altura {altura} es {volumen_cilindro:.2f}")

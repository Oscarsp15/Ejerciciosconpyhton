#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos 
# y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
'''
Fruta	|Precio
--------+-------
Plátano |	1.35
Manzana	|0.80
Pera	|0.85
Naranja	|0.70
'''

# Definir el diccionario de precios de las frutas
precios_frutas = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

# Solicitar al usuario la fruta y la cantidad en kilos
fruta = input("Ingrese el nombre de la fruta: ")
kilos = float(input("Ingrese el número de kilos de fruta: "))

# Verificar si la fruta está en el diccionario
if fruta in precios_frutas:
    # Calcular el precio total
    precio_por_kilo = precios_frutas[fruta]
    precio_total = precio_por_kilo * kilos

    # Mostrar el precio total por pantalla
    print(f"El precio de {kilos} kilos de {fruta} es: {precio_total} euros")
else:
    # Mostrar un mensaje si la fruta no está en el diccionario
    print(f"Lo siento, la fruta {fruta} no está en el diccionario de precios.")

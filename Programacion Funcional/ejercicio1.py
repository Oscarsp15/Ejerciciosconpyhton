#Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, 
# y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos 
# de la cesta y devolver el precio final de la cesta.

# Función para aplicar un descuento a un precio
def aplicar_descuento(precio, porcentaje_descuento):
    descuento = precio * (porcentaje_descuento / 100)
    precio_final = precio - descuento
    return precio_final

# Función para aplicar el IVA a un precio
def aplicar_iva(precio, porcentaje_iva):
    precio_final = precio * (1 + porcentaje_iva / 100)
    return precio_final

# Función para calcular el precio final de una cesta de compra
def calcular_precio_final(cesta, funcion_aplicar):
    precio_total = 0
    for producto, (precio, porcentaje) in cesta.items():
        precio_final_producto = funcion_aplicar(precio, porcentaje)
        precio_total += precio_final_producto
    return precio_total

# Ejemplo de uso
cesta_compra = {
    'producto1': (100, 10),  # (precio, porcentaje para descuento o IVA)
    'producto2': (50, 21),
    'producto3': (200, 0),
}

# Calcular el precio final aplicando descuento
precio_final_descuento = calcular_precio_final(cesta_compra, aplicar_descuento)
print(f"Precio final de la cesta con descuento: {precio_final_descuento}")

# Calcular el precio final aplicando IVA
precio_final_iva = calcular_precio_final(cesta_compra, aplicar_iva)
print(f"Precio final de la cesta con IVA: {precio_final_iva}")

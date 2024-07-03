#Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
#  y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 21%.

# Creando la función
def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total_factura = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total_factura

# Usando la función
print(calcular_total_factura(100))        # Debería devolver 121.0 (aplica 21% de IVA por defecto)
print(calcular_total_factura(100, 10))    # Debería devolver 110.0 (aplica 10% de IVA)
print(calcular_total_factura(200, 18))    # Debería devolver 236.0 (aplica 18% de IVA)

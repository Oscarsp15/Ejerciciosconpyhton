# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

deposito_inicial = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))
tasa_interes = 0.04
balance_ano1 = deposito_inicial * (1 + tasa_interes)
balance_ano2 = balance_ano1 * (1 + tasa_interes)
balance_ano3 = balance_ano2 * (1 + tasa_interes)
balance_ano1 = round(balance_ano1, 2)
balance_ano2 = round(balance_ano2, 2)
balance_ano3 = round(balance_ano3, 2)

print(f"Balance tras el primer año: {balance_ano1}")
print(f"Balance tras el segundo año: {balance_ano2}")
print(f"Balance tras el tercer año: {balance_ano3}")

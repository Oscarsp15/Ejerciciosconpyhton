#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.
precio_habitual = 3.49
descuento = 0.60
barras_no_dia = int(input("Introduce el número de barras vendidas que no son del día: "))
precio_descuento = precio_habitual * (1 - descuento)
coste_final = barras_no_dia * precio_descuento
print(f"Precio habitual de una barra de pan: {precio_habitual}€")
print(f"Descuento aplicado por no ser fresca: {descuento * 100}%")
print(f"Coste final total: {coste_final:.2f}€")

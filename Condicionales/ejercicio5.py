#Para tributar un determinado impuesto se debe ser mayor de 16 años 
# y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
# y muestre por pantalla si el usuario tiene que tributar o no.

# Pedir al usuario su edad
edad = int(input("Introduce tu edad: \n"))

# Pedir al usuario sus ingresos mensuales (para la moneda utilizo float)
ingresos = float(input("Introduce tus ingresos mensuales en euros: "))

# Verificar si el usuario tiene que tributar
if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")

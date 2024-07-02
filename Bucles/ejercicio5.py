#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
#y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Pedir al usuario la cantidad a invertir, el interés anual y el número de años
cantidad = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (%): "))
num_anios = int(input("Introduce el número de años de la inversión: "))

# Convertir el interés anual de porcentaje a decimal
interes_decimal = interes_anual / 100

# Mostrar encabezado de la tabla de resultados
print("\nAño   |   Capital obtenido")

# Calcular y mostrar el capital obtenido cada año
for anio in range(1, num_anios + 1):
    capital_obtenido = cantidad * (1 + interes_decimal)**anio
    print(f"{anio}     |   {capital_obtenido:.2f} €")



#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.

inversion = float(input("¿Cuanto deseas invertir?: \n"))
interes_anual = float(input("¿Cuál es el interés anual?: \n")) 
numero_anios = int(input("¿Cuantos años quiere de inversión?: \n")) 

capital = round(inversion * (interes_anual / 100 + 1) ** numero_anios, 2)


print(f"La capital obtenida para la inversion es: {capital}")

                  

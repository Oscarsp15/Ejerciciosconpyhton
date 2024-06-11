#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
# calculado redondeado con dos decimales.

peso = float(input("Escribe tu peso en kg: \n"))
estatura =  float (input("Escribe tu estatura en m: \n"))
indice = round(peso/estatura**2,2)
print(f"tu indice de masa corporal es: {indice}")

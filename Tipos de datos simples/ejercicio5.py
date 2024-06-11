#Escribir un programa que pregunte al usuario por el número de 
#horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

Htrabajadas = float(input("¿cuantos horas tienes trabajadas?: \n"))
CxHora= float(input("¿cuanto es el coste por hora?: \n"))
pago = Htrabajadas * CxHora
print (f"Tu pago es: S./{pago}") #Utilizo la moneda de mi peru el sol peruano "PEN"
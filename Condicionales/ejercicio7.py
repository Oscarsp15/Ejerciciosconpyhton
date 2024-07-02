#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
'''
Renta	                |Tipo impositivo
------------------------+---------------
Menos de 10000€         |5%
Entre 10000€ y 20000€	|15%
Entre 20000€ y 35000€	|20%
Entre 35000€ y 60000€	|30%
Más de 60000€        	|45%
'''
#Escribir un programa que pregunte al usuario su renta anual 
# y muestre por pantalla el tipo impositivo que le corresponde.

# Pedir al usuario su renta anual
renta = float(input("Introduce tu renta anual en euros: "))

# Determinar el tipo impositivo según los tramos de renta
if renta < 10000:
    tipo_impositivo = 5
elif 10000 <= renta < 20000:
    tipo_impositivo = 15
elif 20000 <= renta < 35000:
    tipo_impositivo = 20
elif 35000 <= renta < 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45

# Mostrar por pantalla el tipo impositivo que le corresponde
print(f"Tu tipo impositivo es del {tipo_impositivo}%.")

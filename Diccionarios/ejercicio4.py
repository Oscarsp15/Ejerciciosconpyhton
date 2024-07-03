#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
# y muestre por pantalla la misma fecha 
# en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

import datetime #importar el modulo datetime

# Solicitar la fecha al usuario en formato dd/mm/aaaa
fecha_str = input("Ingrese una fecha en formato dd/mm/aaaa: ")

try:
    # Convertir la cadena de texto a objeto datetime
    fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
    
    # Obtener el nombre del mes
    nombre_mes = fecha.strftime("%B")  # %B devuelve el nombre completo del mes
    
    # Formatear la fecha en el formato requerido
    fecha_formateada = fecha.strftime(f"%d de {nombre_mes} de %Y")
    
    # Mostrar la fecha formateada por pantalla
    print(fecha_formateada)

except ValueError:
    print("Formato de fecha incorrecto. Debe ser dd/mm/aaaa.")

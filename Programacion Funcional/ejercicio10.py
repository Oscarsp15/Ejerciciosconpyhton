'''
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5



'''


def buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto):
    lista_resultado = []
    
    for inmueble in lista_inmuebles:
        metros = inmueble['metros']
        habitaciones = inmueble['habitaciones']
        garaje = 1 if inmueble['garaje'] else 0  # 1 si tiene garaje, 0 si no
        año_actual = 2024  # Asumiendo que el año actual es 2024
        
        # Calcular la antigüedad del inmueble
        antiguedad = año_actual - inmueble['año']
        
        # Calcular el precio según la zona
        if inmueble['zona'] == 'A':
            precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100)
        elif inmueble['zona'] == 'B':
            precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100) * 1.5
        
        # Añadir el precio al diccionario del inmueble
        inmueble['precio'] = round(precio, 2)  # Redondear el precio a dos decimales
        
        # Si el precio del inmueble es menor o igual al presupuesto dado, añadirlo a la lista de resultados
        if precio <= presupuesto:
            lista_resultado.append(inmueble)
    
    return lista_resultado

# Ejemplo de uso con la lista de inmuebles proporcionada en la pregunta
inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

presupuesto = 100000  # Presupuesto máximo para buscar inmuebles

resultado = buscar_inmuebles_por_presupuesto(inmuebles, presupuesto)

# Imprimir el resultado
print("Inmuebles encontrados dentro del presupuesto:")
for inmueble in resultado:
    print(inmueble)

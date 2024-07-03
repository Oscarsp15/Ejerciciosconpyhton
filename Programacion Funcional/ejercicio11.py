#Escribir una función que reciba una muestra de números y devuelva los valores atípicos, 
# es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. 
# Nota: La puntuación típica de un valor se obtiene restando la media 
# y dividiendo por la desviación típica de la muestra.


import statistics #https://docs.python.org/3/library/statistics.html

def valores_atipicos(muestra):
    # Calcular la media y la desviación estándar de la muestra
    media = statistics.mean(muestra)
    desviacion_estandar = statistics.stdev(muestra)
    
    # Calcular los límites para valores atípicos
    limite_superior = media + 3 * desviacion_estandar
    limite_inferior = media - 3 * desviacion_estandar
    
    # Encontrar los valores atípicos
    valores_atipicos = [valor for valor in muestra if valor > limite_superior or valor < limite_inferior]
    
    return valores_atipicos

# Ejemplo de uso
muestra_numeros = [12, 15, 14, 13, 12, 11, 100, 9, 8, 12, 11, 10, 300]
valores_atipicos_encontrados = valores_atipicos(muestra_numeros)
print("Valores atípicos encontrados:")
print(valores_atipicos_encontrados)

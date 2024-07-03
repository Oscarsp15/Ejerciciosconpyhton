#Escribir una función que reciba otra función booleana y una lista, 
# y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.

# Función que filtra una lista según una función booleana y devuelve los elementos que cumplen la condición
def filtrar_lista(funcion_booleana, lista):
    return list(filter(funcion_booleana, lista))

# Función booleana de ejemplo: verifica si un número es par
def es_par(numero):
    return numero % 2 == 0

# Lista de prueba
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejemplo de uso de la función filtrar_lista con la función booleana es_par
numeros_pares = filtrar_lista(es_par, numeros)
print("Números pares de la lista:", numeros_pares)

# Función booleana de ejemplo: verifica si una palabra empieza con 'a'
def empieza_con_a(palabra):
    return palabra.startswith('a')

# Lista de prueba
palabras = ['manzana', 'banana', 'pera', 'uva', 'kiwi', 'aguacate']

# Ejemplo de uso de la función filtrar_lista con la función booleana empieza_con_a
palabras_con_a = filtrar_lista(empieza_con_a, palabras)
print("Palabras que empiezan con 'a':", palabras_con_a)




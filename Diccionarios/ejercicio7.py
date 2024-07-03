#Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra 
# y el coste total, con el siguiente formato

'''

Lista de la compra	
-------------------
Artículo 1 |	Precio
Artículo 2 |	Precio
Artículo 3 |    Precio
-------------------
…	…
-------------------
Total	Coste


'''

cesta_compra = {}

# Solicitar artículos y precios hasta que el usuario decida terminar
while True:
    articulo = input("Ingrese el nombre del artículo (o 'fin' para terminar): ")
    
    if articulo.lower() == 'fin':
        break
    
    try:
        precio = float(input(f"Ingrese el precio de '{articulo}': "))
        
        # Añadir el artículo y su precio al diccionario
        cesta_compra[articulo] = precio
        
        # Mostrar el contenido actual de la cesta de la compra
        print("\nContenido actual de la cesta de la compra:")
        print("-------------------")
        for item, price in cesta_compra.items():
            print(f"{item} | {price}")
        print("-------------------\n")
    
    except ValueError:
        print("Error: Por favor ingrese un precio válido.")
        continue

# Mostrar la lista final de la compra y el coste total
print("\nLista de la compra")
print("-------------------")
total_coste = 0
for item, price in cesta_compra.items():
    print(f"{item} | {price}")
    total_coste += price
print("-------------------")
print(f"Total\t| {total_coste}")

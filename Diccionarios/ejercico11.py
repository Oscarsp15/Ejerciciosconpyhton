
#El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, 
# donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. 
# Las líneas se separan con el carácter de cambio de línea \n y la primera línea 
# contiene los nombres de los campos con la información contenida en el directorio.


# Cadena de texto que simula el directorio de clientes
directorio_clientes = """nif;nombre;email;teléfono;descuento
01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5
71476342J;Macarena Ramírez;macarena@mail.com;692839321;8
63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2
98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

# Separar la cadena en líneas
lineas = directorio_clientes.strip().split('\n')

# Extraer los nombres de los campos desde la primera línea
nombres_campos = lineas[0].split(';')

# Inicializar una lista para almacenar los clientes como diccionarios
clientes = []

# Procesar cada línea de datos de cliente
for linea in lineas[1:]:
    datos_cliente = linea.split(';')
    cliente = {}
    for i, nombre_campo in enumerate(nombres_campos):
        cliente[nombre_campo] = datos_cliente[i]
    clientes.append(cliente)

# Mostrar todos los clientes
print("Clientes en el directorio:")
for cliente in clientes:
    print(cliente)

# Ejemplo de búsqueda de cliente por NIF
nif_buscar = '71476342J'
print(f"\nBuscando cliente con NIF {nif_buscar}:")
for cliente in clientes:
    if cliente['nif'] == nif_buscar:
        print(cliente)
        break
else:
    print(f"No se encontró cliente con NIF {nif_buscar}.")

# Diccionario principal para la base de datos de clientes
base_de_datos_clientes = {}

# mejor utilizo funciones para el problema.
# Función para añadir un cliente a la base de datos
def agregar_cliente():
    print("\nAñadir cliente:")
    nif = input("Ingrese el NIF del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    preferente = input("¿Es cliente preferente? (True/False): ").lower() == 'true'
    
    # Crear el diccionario con los datos del cliente
    datos_cliente = {
        'nombre': nombre,
        'dirección': direccion,
        'teléfono': telefono,
        'correo': correo,
        'preferente': preferente
    }
    
    # Añadir el cliente al diccionario principal
    base_de_datos_clientes[nif] = datos_cliente
    print(f"\nCliente con NIF {nif} añadido correctamente.")

# Función para eliminar un cliente de la base de datos
def eliminar_cliente():
    print("\nEliminar cliente:")
    nif = input("Ingrese el NIF del cliente que desea eliminar: ")
    
    if nif in base_de_datos_clientes:
        del base_de_datos_clientes[nif]
        print(f"\nCliente con NIF {nif} eliminado correctamente.")
    else:
        print("\nCliente no encontrado en la base de datos.")

# Función para mostrar los datos de un cliente
def mostrar_cliente():
    print("\nMostrar cliente:")
    nif = input("Ingrese el NIF del cliente que desea mostrar: ")
    
    if nif in base_de_datos_clientes:
        datos_cliente = base_de_datos_clientes[nif]
        print("\nDatos del cliente:")
        print(f"NIF: {nif}")
        for key, value in datos_cliente.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("\nCliente no encontrado en la base de datos.")

# Función para listar todos los clientes de la base de datos
def listar_clientes():
    print("\nListar todos los clientes:")
    if base_de_datos_clientes:
        for nif, datos_cliente in base_de_datos_clientes.items():
            print(f"NIF: {nif}, Nombre: {datos_cliente['nombre']}")
    else:
        print("No hay clientes en la base de datos.")

# Función para listar clientes preferentes de la base de datos
def listar_clientes_preferentes():
    print("\nListar clientes preferentes:")
    clientes_preferentes = [nif for nif, datos_cliente in base_de_datos_clientes.items() if datos_cliente['preferente']]
    
    if clientes_preferentes:
        for nif in clientes_preferentes:
            print(f"NIF: {nif}, Nombre: {base_de_datos_clientes[nif]['nombre']}")
    else:
        print("No hay clientes preferentes en la base de datos.")

# Menú principal del programa
while True:
    print("\nMenú:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    
    opcion = input("Seleccione una opción (1-6): ")
    
    if opcion == '1':
        agregar_cliente()
    elif opcion == '2':
        eliminar_cliente()
    elif opcion == '3':
        mostrar_cliente()
    elif opcion == '4':
        listar_clientes()
    elif opcion == '5':
        listar_clientes_preferentes()
    elif opcion == '6':
        print("\n¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Por favor, seleccione una opción del 1 al 6.")

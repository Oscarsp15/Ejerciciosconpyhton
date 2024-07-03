#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura 
# y el valor el coste de la factura. 
# El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
# Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
# Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento 
# y la cantidad pendiente de cobro.


facturas = {}

# Función para calcular la cantidad cobrada y pendiente
def calcular_cobros():
    cobrado = sum(facturas.values())
    pendiente = total_facturas - cobrado
    return cobrado, pendiente

# Inicializar variables para seguimiento de montos
total_facturas = 0

# Bucle principal
while True:
    print("\nMenú:")
    print("1. Añadir nueva factura")
    print("2. Pagar factura existente")
    print("3. Terminar")
    
    opcion = input("Seleccione una opción (1, 2, 3): ")
    
    if opcion == '1':
        # Añadir nueva factura
        numero_factura = input("Ingrese el número de factura: ")
        coste_factura = float(input("Ingrese el coste de la factura: "))
        
        facturas[numero_factura] = coste_factura
        total_facturas += coste_factura
        
        cobrado, pendiente = calcular_cobros()
        
        print(f"\nCantidad cobrada hasta el momento: {cobrado}")
        print(f"Cantidad pendiente de cobro: {pendiente}")
        
    elif opcion == '2':
        # Pagar factura existente
        numero_factura = input("Ingrese el número de factura a pagar: ")
        
        if numero_factura in facturas:
            coste_factura = facturas.pop(numero_factura)
            total_facturas -= coste_factura
            
            cobrado, pendiente = calcular_cobros()
            
            print(f"\nFactura {numero_factura} pagada.")
            print(f"Cantidad cobrada hasta el momento: {cobrado}")
            print(f"Cantidad pendiente de cobro: {pendiente}")
        else:
            print("\nLa factura no existe en el sistema.")
    
    elif opcion == '3':
        # Terminar el programa
        print("\n¡Hasta luego!")
        break
    
    else:
        print("\nOpción no válida. Por favor, seleccione 1, 2 o 3.")

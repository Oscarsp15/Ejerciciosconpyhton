#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

# Mostrar opciones al usuario
print("Bienvenido a la pizzería Bella Napoli.")
print("--------------------------------------")
print("¿Qué tipo de pizza deseas?")
print("1. Pizza vegetariana")
print("2. Pizza no vegetariana")
print("--------------------------------------")
# Pedir al usuario que elija el tipo de pizza
opcion = input("Introduce el número de la pizza que deseas (1 o 2): ")

# Definir ingredientes base comunes a todas las pizzas
ingredientes_base = ["mozzarella", "tomate"]

# Según la opción elegida, mostrar ingredientes disponibles
if opcion == '1':  # Pizza vegetariana
    print("Ingredientes disponibles para pizza vegetariana:")
    print("------------------------------------------------")
    print("1. Pimiento")
    print("2. Tofu")
    print("------------------------------------------------")
    opcion_ingrediente = input("Elige un ingrediente (1 o 2): ")
    
    if opcion_ingrediente == '1':
        ingredientes_elegidos = ingredientes_base + ["pimiento"]
    elif opcion_ingrediente == '2':
        ingredientes_elegidos = ingredientes_base + ["tofu"]
    else:
        print("Opción no válida. Se seleccionará por defecto el ingrediente número 1.")
        ingredientes_elegidos = ingredientes_base + ["pimiento"]

    tipo_pizza = "vegetariana"

elif opcion == '2':  # Pizza no vegetariana
    print("Ingredientes disponibles para pizza no vegetariana:")
    print("---------------------------------------------------")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    print("---------------------------------------------------")
    opcion_ingrediente = input("Elige un ingrediente (1, 2 o 3): ")
    
    if opcion_ingrediente == '1':
        ingredientes_elegidos = ingredientes_base + ["peperoni"]
    elif opcion_ingrediente == '2':
        ingredientes_elegidos = ingredientes_base + ["jamón"]
    elif opcion_ingrediente == '3':
        ingredientes_elegidos = ingredientes_base + ["salmón"]
    else:
        print("Opción no válida. Se seleccionará por defecto el ingrediente número 1.")
        ingredientes_elegidos = ingredientes_base + ["peperoni"]

    tipo_pizza = "no vegetariana"

else:
    print("Opción no válida. Se seleccionará por defecto la pizza vegetariana con pimiento.")
    ingredientes_elegidos = ingredientes_base + ["pimiento"]
    tipo_pizza = "vegetariana"

# Mostrar resultado final
print(f"Has elegido una pizza {tipo_pizza} con los siguientes ingredientes:")
print(", ".join(ingredientes_elegidos))

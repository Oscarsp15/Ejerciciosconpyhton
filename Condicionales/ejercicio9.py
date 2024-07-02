#Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# l programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y
#  si es mayor de 18 años, 10€.


#la edad del cliente
edad = int(input("Introduce la edad del cliente: "))

# Calcular el precio de la entrada según la edad
if edad < 4:
    precio_entrada = 0  # Entrada gratis para menores de 4 años
elif 4 <= edad <= 18:
    precio_entrada = 5  # Precio de 5€ para clientes entre 4 y 18 años
else:
    precio_entrada = 10  # Precio de 10€ para clientes mayores de 18 años

# Mostrar por pantalla el precio de la entrada
print(f"El precio de la entrada para el cliente de {edad} años es de {precio_entrada}€.")

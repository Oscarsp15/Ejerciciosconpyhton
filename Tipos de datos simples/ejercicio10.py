#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso 
# de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos 
# en el último pedido y calcule el peso total del paquete que será enviado.
nromuneca = int(input("Escribe el nro de payasos que se van enviar \n"))
nropayaso = int(input("Escribe el nro de muñecas que se van a enviar \n"))
pesomuneca = float(nromuneca * 112)
pesopayaso = float(nropayaso * 75)
pesototal = pesomuneca + pesopayaso
print(f"El peso total del pedido que se va a enviar es: {pesototal} g")


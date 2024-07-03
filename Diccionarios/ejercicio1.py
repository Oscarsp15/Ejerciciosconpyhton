#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

#divisas alamacenadas en un diccionario
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

#preguntar al usuario
moneda = input("Introduce una divisa : ")

#comprobar si la moneda esta en el diccionario
if moneda in monedas.keys():
        print(monedas[moneda])
else:
        print("No existe esa moneda")

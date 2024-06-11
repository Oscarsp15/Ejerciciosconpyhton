#Escribir un programa que pida al usuario dos números enteros 
# y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.


n1 = int(input("Escribe un numero entero: \n"))
n2 = int(input("Escribe otro numero entero: \n"))
c = n1//n2
r = n1%n2
print(f"El conciente de los dos numeros es: {c} y el resto es: {r} ")
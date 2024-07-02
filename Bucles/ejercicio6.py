#Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

altura = int(input("Introduce un número entero para la altura del triángulo: "))

# Mostrar el triángulo rectángulo
for i in range(1, altura + 1):
    print('*' * i)

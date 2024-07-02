
#Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla el número de veces que contiene cada vocal.


palabra = input("Ingrese una palabra: ")

# Convertir la palabra a minúsculas para ignorar diferencias de mayúsculas y minúsculas
palabra = palabra.lower()

# Inicializar contadores para cada vocal
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

# Iterar sobre cada carácter de la palabra y contar las vocales
for letra in palabra:
    if letra == 'a':
        contador_a += 1
    elif letra == 'e':
        contador_e += 1
    elif letra == 'i':
        contador_i += 1
    elif letra == 'o':
        contador_o += 1
    elif letra == 'u':
        contador_u += 1

# Mostrar por pantalla el número de veces que aparece cada vocal
print(f"Número de veces que aparece cada vocal en la palabra '{palabra}':")
print(f"a: {contador_a}")
print(f"e: {contador_e}")
print(f"i: {contador_i}")
print(f"o: {contador_o}")
print(f"u: {contador_u}")

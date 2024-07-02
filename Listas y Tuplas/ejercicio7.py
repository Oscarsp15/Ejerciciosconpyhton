#Escribir un programa que almacene el abecedario en una lista, 
# elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
# y muestre por pantalla la lista resultante.

# Almacenar el abecedario en una lista
abecedario = list("abcdefghijklmnopqrstuvwxyz")

# Crear una lista para almacenar el resultado
resultado = []

# Iterar sobre el abecedario y eliminar las letras en posiciones múltiplos de 3
for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:  # Verificar si la posición no es múltiplo de 3
        resultado.append(abecedario[i])

# Mostrar por pantalla la lista resultante
print("Abecedario con letras en posiciones no múltiplos de 3:")
print(resultado)

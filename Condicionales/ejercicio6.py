#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M 
# y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.

# Pedir al usuario su nombre
nombre = input("Introduce tu nombre: ")

# Pedir al usuario su sexo
sexo = input("Introduce tu sexo (M para masculino, F para femenino): ")

# Determinar el grupo al que pertenece
if (sexo.upper() == 'F' and nombre.upper() < 'M') or (sexo.upper() == 'M' and nombre.upper() > 'N'):
    grupo = 'A'
else:
    grupo = 'B'

# Mostrar por pantalla el grupo que le corresponde
print(f"Te corresponde el grupo {grupo}.")

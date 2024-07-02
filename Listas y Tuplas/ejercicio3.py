#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia 
# y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
# es cada una des las asignaturas de la lista 
# y <nota> cada una de las correspondientes notas introducidas por el usuario.


# Almacenar las asignaturas en una lista
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Crear una lista vacía para almacenar las notas
notas = []

# Pedir al usuario la nota de cada asignatura
for asignatura in asignaturas:
    nota = input(f"Introduce la nota de {asignatura}: ")
    notas.append(nota)

# Mostrar las asignaturas y las notas ingresadas por el usuario
print("Notas del curso:")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")

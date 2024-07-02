#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
# Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura 
# y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Crear una lista para almacenar las asignaturas aprobadas
aprobadas = []

# Iterar sobre cada asignatura y preguntar la nota al usuario
for asignatura in asignaturas:
    nota = float(input(f"Introduce la nota de {asignatura}: "))
    if nota >= 5.0:
        aprobadas.append(asignatura)  # Añadir a la lista de aprobadas si nota >= 5.0

# Crear una lista con las asignaturas que se deben repetir
repetir = [asig for asig in asignaturas if asig not in aprobadas]

if repetir != []:
# Mostrar por pantalla las asignaturas que se deben repetir
    print("Asignaturas que debes repetir:")
    for asignatura in repetir:
        print(asignatura)
else: 
    print("No tienes asignaturas que repetir")

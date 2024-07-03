#Escribir una función reciba un diccionario con las asignaturas 
# y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas 
# y las calificaciones correspondientes a las notas aprobadas.

# Función que convierte una nota en una calificación
def nota_a_calificacion(nota):
    if nota >= 90:
        return 'A'
    elif nota >= 80:
        return 'B'
    elif nota >= 70:
        return 'C'
    elif nota >= 60:
        return 'D'
    else:
        return 'F'

# Función que recibe un diccionario con asignaturas y notas, y devuelve otro diccionario con asignaturas en mayúsculas y calificaciones de notas aprobadas
def asignaturas_aprobadas(asignaturas_notas):
    asignaturas_calificaciones = {}
    for asignatura, nota in asignaturas_notas.items():
        if nota >= 60:  # Filtrar solo las notas aprobadas
            asignatura_mayusculas = asignatura.upper()
            calificacion = nota_a_calificacion(nota)
            asignaturas_calificaciones[asignatura_mayusculas] = calificacion
    return asignaturas_calificaciones

# Ejemplo de uso
asignaturas_notas = {
    'matemáticas': 85,
    'ciencias': 92,
    'historia': 78,
    'literatura': 60,
    'educación física': 45,
    'arte': 88,
    'informática': 72
}

calificaciones_aprobadas = asignaturas_aprobadas(asignaturas_notas)
print("Calificaciones correspondientes a las asignaturas aprobadas:")
print(calificaciones_aprobadas)

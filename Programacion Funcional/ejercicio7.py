#Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno 
# y devuelva otro diccionario con las asignaturas en mayúsculas 
# y las calificaciones correspondientes a las notas.


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

# Función que recibe un diccionario con asignaturas y notas, y devuelve otro diccionario con asignaturas en mayúsculas y calificaciones
def asignaturas_a_calificaciones(asignaturas_notas):
    asignaturas_calificaciones = {}
    for asignatura, nota in asignaturas_notas.items():
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

calificaciones = asignaturas_a_calificaciones(asignaturas_notas)
print("Calificaciones correspondientes a las asignaturas:")
print(calificaciones)

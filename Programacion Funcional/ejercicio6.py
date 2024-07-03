#Escribir una función reciba una lista de notas 
# y devuelva la lista de calificaciones correspondientes a esas notas.

# Función que convierte una lista de notas en una lista de calificaciones, considero hasta 100
def notas_a_calificaciones(notas):
    calificaciones = []
    for nota in notas:
        if nota >= 90:
            calificaciones.append('A')
        elif nota >= 80:
            calificaciones.append('B')
        elif nota >= 70:
            calificaciones.append('C')
        elif nota >= 60:
            calificaciones.append('D')
        else:
            calificaciones.append('F')
    return calificaciones

# Ejemplo de uso
notas = [85, 92, 78, 60, 45, 88, 72]
calificaciones = notas_a_calificaciones(notas)
print("Calificaciones correspondientes a las notas:")
print(calificaciones)

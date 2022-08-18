# Estructura selectiva simple (if)
"""
selectiva_simple_2.py
Script en Python que solicite la calificacion y cantidad de asistencias a un curso. si la calificacion es mayor o igual que 60  y la cantidad de asistencia es mayor a 20 entonces aprobo el curso.
"""

calificacion = int(input('Cual es tu calificacion? '))
asistencias = int(input('Cuantas asistencias tuviste? '))

if calificacion >= 60 and asistencias >= 20:
    print('Felicitaciones aprobaste el curso!')

print('Sigue disfrutando tu dia.')
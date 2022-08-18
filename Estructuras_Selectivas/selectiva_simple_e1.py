'''
selectiva_simple_e1.py
Script en Python que implemente un sistema de redondeo de calificaciones.
'''

calificacion = int(input('Cual es tu calificacion? __'))
residuo = calificacion % 10
mensaje = ' Tu calificacion no amerita redondeo.'

if residuo >= 6:
    calificacion = calificacion + (10 - residuo)
    mensaje = f'Tu calificacion es: {calificacion}'

print(mensaje)
print('adios ')
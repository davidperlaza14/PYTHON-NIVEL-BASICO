# ESTRUCTURA SELECTIVA MULTIPLES - if elif elif... else
'''
script en Python que solicite al usuario una calificacion y una cantidad de asistencias a un curso. Si la calificacion y la cantidad de asistencias son aprobatorias entonces se le felicita por su logro.
calificacion para aprobar 60
asistencias para aprobar 24
'''

MIN_CAL = 60
MIN_ASI = 24

print("Por favor ingresa los siguientes datos: ")
cal = int(input("Calificacion: "))
asi = int(input("Asistencias: "))

if cal >= MIN_CAL and asi >= MIN_ASI:
    print("Felicidades aprobaste el curso!")
elif cal < MIN_CAL and asi >= MIN_ASI:
    print(f"Reprobaste porque la calificacion minima era {MIN_CAL} y tu sacaste {cal}")
elif cal >= MIN_CAL and asi < MIN_ASI:
    print(f"Reprobaste porque las asistencias minimas eran {MIN_ASI} y tu solo asististe {asi}")
else:
    print(f"Tu calificacion fue {cal} y tus asistencias fueron {asi}, por dicha razon no aprobaste el curso.")
print("Espero tengas un buen dia. Saludos!")
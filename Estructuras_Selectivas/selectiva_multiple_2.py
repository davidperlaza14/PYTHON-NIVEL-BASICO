# ESTRUCTURA SELECTIVA MULTIPLES - if elif elif... else
'''
script en Python que muestre un menu con los nombre de distintos paises de america y si el usuario selecciona alguna de las opciones se le mostrara el nombre de la capital de ese pais.
'''
MEXICO = 1
URUGUAY = 2
COLOMBIA = 3
ARGENTINA = 4
PERU = 5
ECUADOR = 6

print("""\n                   Capitales de America

Elige un pais y te dire su capital.

1) Mexico
2) Uruguay
3) Colombia
4) Argentina
5) Peru
6) Ecuador
""")
opc = int(input("Selecciona una opcion:__"))

if opc == MEXICO:
    print("Ciudad de Mexico")
elif opc == URUGUAY:
    print("Montevideo")
elif opc == COLOMBIA:
    print("Bogota")
elif opc == ARGENTINA:
    print("Buenos Aires")
elif opc == PERU:
    print("Lima")
elif opc == ECUADOR:
    print("Quito")
else:
    print("Opcion no valida.")
print("Que tengas un buen dia.")
'''
procedimientos_4.py
script de Python que muestre un menu ciclico; dicho menu sera implementado en un procedimiento.s
'''
import os

ESP = 1
ENG = 2
NO_SUB = 3
SALIR = 4

def mostrar_menu():

    print(f"""\n                              Subtitulos
    {ESP}) Espanol
    {ENG}) Ingles
    {NO_SUB}) Sin subtitulos
    {SALIR}) Salir
    """)

continuar = True
while continuar:
    os.system("clear")
    mostrar_menu()
    opc = int(input("Selecciona una opcion: "))
    os.system("clear")
    if opc == ESP:
        print("Subtitulos en espanol")
    elif opc == ENG:
        print("Subtitulos en ingles")
    elif opc == NO_SUB:
        print("Subtitulos apagados")
    elif opc == SALIR:
        continuar = False
    else:
        print("Opcion no valida")
    input("Presiona enter para continuar...")

print("Nos vemos...")
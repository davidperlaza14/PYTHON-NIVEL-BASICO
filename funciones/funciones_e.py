"""
funciones_e.py
script en python que implemente un programa para realizar las suiguientesconversuines:
- segundos a minutos: secibe segundos y devuelve minutos y segundos
- segundos a horas: recibe segundos y regresa horas, minutos y segundos
- minutos a segundo: recibe minutos y segundos y regresa segundos
- minutos a horas: recibe minutos y segundos y regresa horas minutos y segundos
Ademas debera implementarse un metodo para imprimir el menu de opciones y la ejecucion del programa debe comenzar desde el procedimiento "main".
El programa debe seguir en ejecucion mientras el usuario no decida salir.
"""

import os

SEGUNDOS_POR_MINUTO = 60
MINUTOS_POR_HORA = 60
SEGUNDO_A_MINUTOS = 1
SEGUNDO_A_HORAS = 2
MINUTOS_A_SEGUNDOS = 3
MINUTOS_A_HORAS = 4
SALIR = 0

def segundo_a_minutos(segundos):
    mins = segundos // SEGUNDOS_POR_MINUTO
    segs = segundos % SEGUNDOS_POR_MINUTO

    return mins, segs

def minutos_a_segundos(minutos, segundos):
    segs = minutos * SEGUNDOS_POR_MINUTO + segundos

    return segs

def minutos_a_segundos(minutos, segundos):
    hrs =  minutos // MINUTOS_POR_HORA
    mins = minutos % MINUTOS_POR_HORA
    segs = segundos

    return hrs, mins, segs

def minutos_a_horas(minutos, segundos):
    hrs =  minutos // MINUTOS_POR_HORA
    mins = minutos % MINUTOS_POR_HORA
    segs = segundos

    return hrs, mins, segs

def segundo_a_horas(segundos):
    mins, segs = segundo_a_minutos(segundos)
    hrs, mins, segs = minutos_a_horas(mins,segs)

    return hrs, mins, segs

def menu():
    print(f'''                           Connversiones
{SEGUNDO_A_MINUTOS}) Segundo a minutos
{SEGUNDO_A_HORAS}) Segundo a horas
{MINUTOS_A_SEGUNDOS}) Minutos a segundos
{MINUTOS_A_HORAS}) minutos a horas
{SALIR}) Salir''')

def main():
    continuar = True
    while continuar:
        os.system("clear")
        menu()
        opc = int(input("Seleccion una opcion: "))
        os.system("clear")
        if opc == SEGUNDO_A_MINUTOS:
            s = -1
            while 0 > s:
                s = int(input("Cantidad de segundos a convertir: "))
            mins, segs = segundo_a_minutos(s)
            print(f"El equivalente es {mins}:{segs}")
        elif opc == SEGUNDO_A_HORAS:
            s = -1
            while 0 > s:
                s = int(input("Cantidad de segundos a convertir: "))
            hrs, mins, segs = segundo_a_horas(s)
            print(f"El equivalente es {hrs}:{mins}:{segs}")
        elif opc == MINUTOS_A_SEGUNDOS:
            m = -1
            while 0 > m:
                m = int(input("Cantidad de minutos a convertir: "))
            s = -1
            while 0 > s or s >= SEGUNDOS_POR_MINUTO:
                s = int(input("Cantidad de segundos a convertir: "))
            segs =  minutos_a_segundos(m, s)
            print(f"El equivalente es {segs}")
        elif opc == MINUTOS_A_HORAS:
            m = -1
            while 0 > m:
                m = int(input("Cantidad de minutos a convertir: "))
            s = -1
            while 0 > s or s >= SEGUNDOS_POR_MINUTO:
                s = int(input("Cantidad de segundos a convertir: "))
            hrs, mins, segs = minutos_a_horas(m, s)
            print(f"El equivalente es {hrs}:{mins}:{segs}")
        elif opc == SALIR:
            print("Nos vemos...")
            continuar = False
        else:
            print("Opcion no valida")
        input("Presiona enter para continuar")


if __name__ == "__main__":
    main()

            


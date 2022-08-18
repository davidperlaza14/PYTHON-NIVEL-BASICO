"""
repetitiva_mientras_e.py
Script en Python que implimente el juego de adivinar un numero, pero esta vez en modo competitivo. La computadora debera generar un numero entre 1 y 100 y tanto el usuario como la computadora deberan adivinar dicho numero. Para que el juego sea retador el jugador maquina debera ser "inteligente" y competir para ganar. El juego se realizara por turnos, primero la maquina y luego el usuario  y por cada intento la computadora respondera si el numero es mayor o menor que el secreto.
"""

import os
import random
from re import U

inferior = 1
superior = 100
secreto = random.randint(1, 100)
usuario = -1
maquina = -1


while usuario != secreto and maquina != secreto:
    os.system("clear")
    print("Maquina, Cual crees que sea el numero secreto?")
    maquina = random.randint(inferior, superior)
    print(f"Maquina: {maquina}")
    if maquina < secreto:
        print("Tu numero es menor")
        inferior = maquina + 1
    elif maquina > secreto:
        print("Tu numero es mayor")
        superior = maquina - 1
    else:
        print("La maquina ha ganado, felicitaciones!")
    # input("Presiona enter para continuar...")
    # input(" Nos vemos...")
    if maquina != secreto: 
        usuario = int(input("Usuario, Cual crees que sea el numero secreto?"))
        if usuario < secreto:
            print("Tu numero es menor")
            if usuario > inferior:
                inferior = usuario + 1
        elif usuario > secreto:
            print("Tu numero es mayor")
            if usuario < superior:
                superior = usuario -1
        else:
            print("Has ganado, felicitaciones!")
        input("Presiona enter para continuar...")
input(" Nos vemos...")
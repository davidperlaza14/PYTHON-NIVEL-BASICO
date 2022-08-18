# ESTRUCTURA SELECTIVA DOBLE - IF ELSE
'''
selectiva_doble_1.py
Script de Python que solicite al usuario intente adivinar un numero entre 1 y 10.
'''
import random
from traceback import print_tb

secreto = random.randint(1, 10)
print('Acabo de generar un numero secreto entre 1 y 10.')
usuario = int(input("Cual crees que sea mi numero secreto? "))

if usuario == secreto:
    print('Lograste adivinar mi numero.')
else:
    print(f'El numero secreto es: {secreto}')
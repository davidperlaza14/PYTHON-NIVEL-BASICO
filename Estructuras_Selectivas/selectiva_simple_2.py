# Estructura selectiva simple (if)
"""
selectiva_simple_2.py
Script en Python que genere un numero aleatorio entre 1 y 10 y le pida al usuario que intente adivinarlo.
"""
"""Agrega un modulo random a mi programa y me permite generar numeros aleatorios."""

import random
secreto = random.randint(1, 2)
print("Acabo de generar un numero aleatorio en tre 1 y 10")
numero = int(input("Cual crees que sea mi numero? __"))

if numero == secreto:
 print("lo lograste: Adivin@ mistic@")

print("sigue teniendo un buen dia.")


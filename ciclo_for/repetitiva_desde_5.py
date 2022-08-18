'''
repetitiva_desde_4.py
script de python que muestre las tablas de multiplicar de los numero del 1 al 10. Cada tabla se muestra hasta el decimo multiplo.
'''

from audioop import mul


for numero in range(1, 13):
    print(f"                                Tabla de multiplicar del {numero}")
    for multiplo in range(1, 13):
        print(f"{numero} * {multiplo} = {numero * multiplo}")

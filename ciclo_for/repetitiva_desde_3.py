'''
repetitiva_desde_3.py
script de python que muestre una cuenta regresiva usando un ciclo for y esperando un segundo entre cada numero.
''' 
import os
import time

for numero in range(10, -1, -1):
    os.system("clear")
    print(numero)
    time.sleep(1)
else:
    print("Feliz ano nuevo.")
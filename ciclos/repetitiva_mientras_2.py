"""
repetitiva_mientras_2.py
script de Python que sume valores pares y multiplique valores impares mientras el usuaro no ingrese un 0. se debera utilizar la estructura repetitiva "while" para solicitar al usuario un numero y dependiendo del numero lo suma o lo multiplica.
"""
print("Programa que suma valores pares y multiplica valores impares")

suma = 0
multiplicacion = 1
numero = 1

while numero != 0:
    numero = int(input("Ingrese un numero (0 para salir): "))
    if numero % 2 == 0:
        suma =  suma + numero
    else:
        multiplicacion = multiplicacion * numero
    print(f"suma: {suma}")
    print(f"Multiplicacion: {multiplicacion}")
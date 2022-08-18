'''
repetitiva_desde_4.py
script de python que muestre la tabla de multiplicar de un numero ingresado por el usuario. El usuario tambien podra ingresar hasta que valor llegara la tabla de multiplicar.
'''

numero = int(input("De que numero deseas ver la tabla de multiplicar?: "))
limite = int(input("Hasta que multiplo deseas ver?"))

print(f"                            Tabla del {numero}")
for multiplo in range(1, limite+1):
    print(f"{numero} * {multiplo} = {numero * multiplo}")

print("Nos vemos...")


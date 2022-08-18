'''
funciones_4.py
script en Python que implemente una funcion para calcular el area de un triangulo. Dicha funcion debera recibir como argumentos el valor de  la base y la altura y regresar el area calculada.
'''


def area_triangulo(altura, base):
    return base * altura / 2

print(" Calcular el area de un triangulo")
print("Ingresa los siguientes valores")
altura = float(input("Altura: "))
base = float(input("Base: "))

print(f"\nArea = {area_triangulo(altura, base) :.2f}\n")
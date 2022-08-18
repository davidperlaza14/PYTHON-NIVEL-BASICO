'''
funciones_6.py
script en Python que implemente una funcion encargada de convertir una cantidad de segundos a minutos y segundos. La funcion deberia recibir como argumento una cantidad de segundos y debera regresar la cantidad de minutos y segundos equivalente.
'''

def segundos_a_minutos(segundos):
    m = segundos // 60
    s = segundos % 60
    return m, s

print("Programa que convierte segundos a minutos y segundos")
seg = int(input("Segundos a convertir: "))
min, segu = segundos_a_minutos(seg)

print(f"El equivalente es: {min}:{segu}")

print("Nos vemos...")
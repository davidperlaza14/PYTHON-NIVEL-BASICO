'''
repetitiva_desde_6.py
script de python que pregunte al usuario un cantidad de numeros a registrar, le solicite dichos valores y finalmente imprima el promedio de los mismos.
'''
acumulador = 0
print("Vamos a calcular un promedio.")
total_datos = int (input("Cuantos datos deseas registrar?: "))

for valor in range(total_datos):
    numero = int(input(f"Ingresar el valor  {valor+1}: "))
    acumulador += numero

promedio =  acumulador / total_datos
print(f"El promedio es: {promedio}")

print("Nos vemos...")
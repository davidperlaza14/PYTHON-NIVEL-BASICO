'''
repetitiva_desde_2.py
script de python que  imprima los numeros pares desde el 2 hasta el 20 haciendo uso del ciclo for.
'''

print("Programa que muestre los numeros pares desde el 2 hasta el 20")

print("Metodo 1")
for numero in range(1, 11):
    print(f"par: {numero*2}")
print("\n")
print("*"*40)
print("\n")

print("Metodo 2")
for numero in range(2, 21):
    if numero % 2 == 0:
        print(f"par: {numero}")

print("\n")
print("*"*40)
print("\n")

print("Metodo 3")
for par in range(2, 21, 2):
    print(f"par: {par}")


print("Nos vemos...")

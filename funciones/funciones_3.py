'''
funciones_3.py
script en Python que implemente una funcion encargada de convertir grados Fahrenhit a Celsius.
'''
def convertir_grados():
    print("Convertir grados Fahrenhit a Celsius.")
    F = float(input("Ingresa los grados F: "))
    C =  5 / 9 * (F - 32)
    return C

C = convertir_grados()
print(f"Es igual a {C:.2} grados celsius.")

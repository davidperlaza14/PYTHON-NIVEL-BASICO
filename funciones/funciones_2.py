'''
funciones_2.py
script en Python que implemente una funcion que calcule el indice de masa corporal del usuario.
'''

def calcula_imc():
    peso = float(input("Ingresa tu peso: "))
    altura = float(input("Ingresa tu altura: "))
    imc = peso / altura**2
    return imc


print("Programa para calcular El índice de masa corporal (IMC)")
pa = calcula_imc()
print(f"Tu IMC es: {pa :.2f}")
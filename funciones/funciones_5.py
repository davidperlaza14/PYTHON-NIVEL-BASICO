'''
funciones_5.py
script en Python que implemente una funcion que calcule el indice de masa corporal del usuario. La funcion debe recibir el peso y la estatura del usuario y como resultado regresa el valor de indice de masa corporal.
'''

def calcula_imc(peso, altura):
    return peso / altura**2

print(" Calcular el IMC")
print("Ingresa los siguientes valores")
peso = float(input("Peso: "))
altura = float(input("Altura: "))


print(f"\nIMC = {calcula_imc(peso, altura) :.2f}\n")
print("Nos vemos...")
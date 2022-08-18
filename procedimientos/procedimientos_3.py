'''
procedimientos_3.py
script de Python que dentro de un procedimiento solicite el nombre y la edad del usuario y en caso de ser mayor o igual que 18 le indique que es mayor de edad, en caso contrario indicarle que aun es menor.
'''

def mayoria_edad():
    nombre = input("Hola, como te llamas? ")
    edad = int(input(f"Hola {nombre}! Cual es tu edad? "))
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

mayoria_edad()
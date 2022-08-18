"""
procedimientos_6.py
script de Python que implemente un procedimiento que reciba el nombre y la edad del usuario y en caso que la edad sea mayor o igual que 18 le indique que ya es mayor de edad; en caso contarario le indique que es menor de edad.
"""


def mayoria_edad(nombre, edad):
    print(f"Hola {nombre}, gusto en verte de nuevo.")
    if edad > 18:
        print("Veo que ya eres mayor de edad")
    else:
        print("Veo que aun eres menor de edad")

mayoria_edad("Alis", 17)
"""
procedimientos_7.py
script de Python que implemente un procedimiento  dentro del cual se muestre la  tabla de multiplicar de un numero recibido como argumento. El procedimiento contara con un segundo argumento que indicara hasta que multiplo se mostrara la tabla de multiplicar. Ese segundo argumento se tendra como valor por omision el numero 10.
"""

def tabla_multiplicar(numero, limite=10):
    print(f"                    Table de multiplicar del {numero}")
    for i in range(1, limite+1):
        print(f"{numero} * {i} = {numero * i}")

tabla_multiplicar(7)
tabla_multiplicar(5, 13)

print("Nos vemos...")
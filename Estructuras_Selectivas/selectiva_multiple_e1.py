#  ESTRUCTURA SELECTIVA MULTIPLES - if elif elif... else
"""
script de Python de operadores aritmetricos. Utilizando la estructura selectiva multiple if elif else.
"""

from __future__ import division


SUMA = 1
RESTAR = 2
MULTIPLICAR = 3
DIVISION = 4

print("""\n               Calculadora


1) Suma
2) Resta
3) Multiplicacion
4) Division
""")

opc = int(input("Elige la operacion que deseas realizar: __"))

if opc == SUMA:
    sum1 = int(input("num1: "))
    sum2 = int(input("num2: "))
    suma = sum1 + sum2
    print(f"la suma de {sum1} + {sum2} es: {suma}")
elif  opc == RESTAR:
    res1 = int(input("num1: "))
    res2 = int(input("num2: "))
    resta = res1 - res2
    print(f"la resta de  {res1} - {res2} es: {resta}")
elif  opc == MULTIPLICAR:
    mul1 = int(input("num1: "))
    mul2 = int(input("num2: "))
    multi=  mul1 * mul2
    print(f"el resultado de  {mul1} * {mul2} es: {multi}")

elif  opc == DIVISION:
    print("division")
    div1 = int(input("num1: "))
    div2 = int(input("num2: "))
    if div2 != 0:
        divi = div1 / div2
    
        print(f" El resultado es {div1} / {div2} es: {divi}")
    else:
            print("la division por 0 no esta definida. intenta de nuevo") 

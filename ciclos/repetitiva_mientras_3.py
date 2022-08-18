'''
repetitiva_mientras_3.py
script de Python que simule un sistema de validacion de una plataforma
digital. El usuario debera proporcionar tanto su nombre como su contrasena
mientras la informacion proporcionada no coincida con la informacion previamente registrada.
'''
import os


USER = "S"
PASSWORD = "3"


user = ""
password = " "

while USER != user or PASSWORD != password:
    os.system("clear")
    print("                 kit-kot")
    user = input("Usuario: ")
    password = input("Contrasena: ")

    if USER != user or PASSWORD != password:
        print("Credenciales incorrectas")
        print("Intenta de nuevo")
        input("Presiona enter para continuar")
else:
    print("Bienvenidos...")
input("Nos vemos...")
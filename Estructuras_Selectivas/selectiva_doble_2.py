# ESTRUCTURA SELECTIVA DOBLE - IF ELSE
'''
selectiva_doble_2.py
script de Python que simule un sistema de validacion de una plataforma digital. El usuario debera proporcionar tanto su nombre como su contrasena. Si los valores coinciden con los previamente almacenados se le dara la bienvenida, sino se le indicara que hubo un error.
'''

from curses.ascii import US

from cupshelpers import Printer


USER = 'DAVID123'
PASSWORD = 'DAVID123'

print('Proporciona los siguientes datos: ')
user = input('Usuario: ')
password = input('Contrasena: ')

if user == USER and password == PASSWORD:
    print('                insta[o]')
    print('Bienvenid@ a tu cuenta')
else:
    print('Datos incorrectos, intenta de nuevo.')

print('Que tengas un buen dia')
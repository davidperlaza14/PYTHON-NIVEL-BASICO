'''
procedimientos_2.py
script de Python que implemente un procedimiento para saludar al usuario de manera personalizada; el procedimiento debera  recibir el nombre del usuario como argumento. Se debera crear otro procedimiento llamdo "main" desde el cual se inicie la ejecucion del programa y dentro del cual se solicite el nombre del usuario y se utilice el primer procedimiento descrito. 
'''

def saludo_personal(nombre):
    print(f"Gusto de verde {nombre}")

def main():
    usuario = input('Hola como te llamas?')
    saludo_personal(usuario)

if __name__ == '__main__':
    main()
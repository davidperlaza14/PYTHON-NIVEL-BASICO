'''
repetitiva_desde_6.py
script de Python que muestre un cronometro en formato de 24 horas.
El despliegue seguira el formato h:m:s. El cronometro debera iniciar en 0:0:0 y podra llegar
hasta 23:59:59. Implementar retardo de 1 segundo y limpieza  de pantalla de forma tal que solo se vea un
tiempo en pantalla.
'''

import os
import time
import numpy as np

for hora in range(24):
    for minutos in range(60):
        for segundo in range(60):
            for milesimas in np.arange(100):
                os.system("clear")
                print(f"{hora}:{minutos}:{segundo}:{milesimas}")
                time.sleep(0.01)
                # time.sleep(1)
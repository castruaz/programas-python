# Tabla de multiplicar

import os
while(True):
    os.system('clear')
    t = int(input('Cual Tabla quieres ? '))
    n = int(input('Hasta donde ?'))
    c = 1
    while c <= n:
        print(f'{c} x {t} = {c * t}')
        c += 1
    if input('Deseas otra tabla (S/N) ?').upper()=='N': break
print('Gracias ...')
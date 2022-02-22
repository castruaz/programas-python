# Tabla de multiplicar

while(True):
    t = int(input("Cual Tabla quieres ?"))
    c = 1
    while c <= 10:
        print(f'{c} x {t} = {c * t}')
        c += 1
    if input('Deseas otra tabla (S/N) ?').upper()=='N': break
print('Gracias ...')
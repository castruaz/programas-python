# Muestra el tipo de angulo segun si tamano
# <90 agudo, =90 recto, >90 y <180 obtuso, =180 llano, >180 y <360 concavo

print('Mostrando el tipo de angulo segun su tamano ...')
angulo = int(input('Dame el angulo ?'))
print(f'El angulo es de {angulo} por lo tanto es un angulo: ',end='')
if angulo < 90 :
    print('agudo')
elif angulo == 90:
    print('recto')
elif angulo>90 and angulo<180:
    print('obtuso')
elif angulo==180:
    print('llano')
elif angulo>180 and angulo < 360:
    print('concavo')
else:
    print('angulo fuera de rango')
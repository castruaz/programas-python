# Calcula la segunda ley de newton (f = m * a)
print('Calculando la segunda ley de newton (f = m * a) ...')
print('Calcular la fuerza ....... [f]')
print('Calcular la masa ......... [m]')
print('Calcular la aceleracion... [a]')
op = str.lower(input('Elige una opcion ? '))
if op=='f':
    print('\nCalculando la fuerza ...')
    m = float(input('dame la masa ? '))
    a = float(input('dame la aceleracion ? '))
    f = m * a
    print(f'\nLa fuerza es {f}')
elif op=='m':
    print('\nCalculando la masa ...')
    f = float(input('dame la fuerza ? '))
    a = float(input('dame la aceleracion ? '))
    m = f / a
    print(f'\nLa masa es {m}')
elif op=='a':
    print('\nCalculando la aceleracion ...')
    f = float(input('dame la fuerza ? '))
    m = float(input('dame la masa ? '))
    a = f / m
    print(f'\nLa aceleracion es {a}')
else:
    print('\nElegiste una opcion invalida ..')
print('\nPrograma terminado, muchas gracias ...')

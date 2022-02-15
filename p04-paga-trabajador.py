# Calcula la paga de un trabajador

# Entrada
print('Calculando la paga de un trabajador ..')
nombre = input('Nombre del trabajador ? ')
horas  = int(input('Horas trabajas ?'))
paga   = float(input('Paga por hora ? '))
tasa   = 0.3
# Proceso
pagabruta = horas * paga
impuesto  = pagabruta * 0.3
paganeta  = pagabruta - impuesto
# Salida
print('Resumen de pagos :')
print(f'El trabajador {nombre} trabajo {horas} horas, con pago de {paga} pesos la hora y una tasa de {tasa}% de impuesto')
print(f'Paga bruta : {pagabruta}')
print(f'Impuesto   : {impuesto}')
print(f'Paga neta  : {paganeta}')

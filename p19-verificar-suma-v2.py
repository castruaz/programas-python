# Verificar si la suma de dos numeros es igual a un tercero
# 10 20 30   10 30 20   30 10 20    ( 30 30 30     9 8 7   1 3 5   1 1 3 ) 

print('Verificando si la suma de dos numeros es igual a un tercero ...')
print('Dame 3 numeros enteros separados por una linea:')
n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int(n2), int(n3)]
if n1+n2==n3:
    print('n1+n2=n3')
elif n1+n3==n2:
    print('n1+n3=n2')
elif n2+n3==n1:
    print('n2+n3=n1')
else:
    print('no hay sumas que coincidan')
 
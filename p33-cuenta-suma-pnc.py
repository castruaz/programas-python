# cuenta y suma, numeros positivos negativos y ceros

c=s=cp=cn=cc=0
while True:
    n = int(input('Numero? '))
    if n == 999 : break
    s += n
    c += 1
    if n>0 :     cp+=1
    elif n<0 :   cn+=1
    else :       cc+=1
print('Se introdujeron {0}'.format(c))
print('Pos: {0}, Neg: {1}, Ceros: {2}'.format(cp,cn,cc))
print('La suma de los numeros es {0}'.format(s))
# numeros de 1 a n

c = 1
n = int(input('Hasta donde ? '))
while c <= n :
    c += 1
    if c % 5 != 0:
        continue
    print(c, end=' ')
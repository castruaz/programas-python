# numeros de 1 a 200, hasta sumar 1000
# 1 + 2 + 3 + 4 >= 100

c = 0
s = 0
while c < 200:
    c += 1
    s += c
    print(c, end=' ')
    if s >= 1000 :
        print('\n')
        break
print(f'Hemos alcanzanzado la suma {s}')


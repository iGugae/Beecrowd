A, B, C, D = input().split()
a = int(A)
b = int(B)
c = int(C)
d = int(D)

if (b > c and d > a and (c + d) > (a + b) and c >= 0 and d >= 0 and a % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

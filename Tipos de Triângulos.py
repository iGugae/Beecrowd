lista = A, B, C = input().split()
lista.sort(key=float, reverse=True)
a = float(lista[0])
b = float(lista[1])
c = float(lista[2])

if (a >= (b+c)):
    print('NAO FORMA TRIANGULO')
if (a**2 == (b**2 + c**2) and a < (b+c)):
    print('TRIANGULO RETANGULO')
if (a**2 > (b**2 + c**2) and a < (b+c)):
    print('TRIANGULO OBTUSANGULO')
if (a**2 < (b**2 + c**2) and a < (b+c)):
    print('TRIANGULO ACUTANGULO')
if (a == b == c and a < (b+c)):
    print('TRIANGULO EQUILATERO')
elif (a == b or a == c or b == c and a < (b+c)):
    print('TRIANGULO ISOSCELES')

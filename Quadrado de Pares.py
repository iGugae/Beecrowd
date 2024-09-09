valor = int(input())
quadrado = 0

for i in range(1,valor+1):
    if (i % 2 == 0):
        quadrado = i ** 2
        print(f'{i}^2 = {quadrado}')

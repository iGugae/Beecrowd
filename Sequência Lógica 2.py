X, Y = input().split()

x = int(X)
y = int(Y)

contador = 1
for i in range(1,y+1):
    if (contador % x == 0):
        print(f'{i}')
    else:
        print(f'{i}', end=' ')
    contador +=1

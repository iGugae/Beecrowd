resultado = [ ]
while True:
    X, Y = input().split()
    x = int(X)
    y = int(Y)

    if (x > y):
        resultado.append('Decrescente')
    elif (y > x):
        resultado.append('Crescente')
    else:
        break

for i in resultado:
    print(i)

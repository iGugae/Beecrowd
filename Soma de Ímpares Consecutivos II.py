n = int(input())
somas = [ ]

for i in range(0,n):
    X, Y = input().split()
    x = int(X)
    y = int(Y)
    soma = 0

    if (x < y):
        for i in range(x+1,y):
            if (i % 2 != 0):
                soma += i
    else:
        for i in range(y+1,x):
            if (i % 2 != 0):
                soma += i
    somas.append(soma)

for i in somas:
    print(i)

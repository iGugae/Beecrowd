n = int(input())

for i in range (0,n):
    X, Y = input().split()
    x = int(X)
    y = int(Y)
    soma = 0
    num = 0

    while True:
        if (x % 2 != 0):
            num = x
            for i in range(0,y):
                soma += num
                num += 2
            break
        else:
            num = x + 1
            for i in range(0,y):
                soma += num
                num += 2
            break

    print(soma)

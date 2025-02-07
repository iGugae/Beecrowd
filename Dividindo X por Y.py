num = int(input())

for i in range(num):
    X, Y = input().split()
    x = int(X)
    y = int(Y)
    res = 0

    if (y == 0):
        print('divisao impossivel')
    else:
        res = x/y
        print(res)

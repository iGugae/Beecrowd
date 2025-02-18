while True:
    x = int(input())
    soma = 0

    if (x == 0):
        break
    else:
        for i in range(x,(x+10)):
            if (i % 2 == 0):
                soma += i
    print(soma)

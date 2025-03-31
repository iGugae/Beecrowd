num = int(input())
total = 0

for i in range(0,num):
    a, b = input().split()
    codigo = int(a)
    quant = int(b)

    if (codigo == 1001):
        preco = 1.5
    elif (codigo == 1002):
        preco = 2.5
    elif (codigo == 1003):
        preco = 3.5
    elif (codigo == 1004):
        preco = 4.5
    else:
        preco = 5.5
    
    total += (preco*quant)

print(f"{total:.2f}")

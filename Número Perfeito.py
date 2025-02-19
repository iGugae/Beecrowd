n = int(input())

for i in range(0,n):
    num = int(input())
    soma = 0

    for i in range(1,num):
        if (num % i == 0):
            soma += i
    
    if (soma == num):
        print(f'{num} eh perfeito')
    else:
        print(f'{num} nao eh perfeito')

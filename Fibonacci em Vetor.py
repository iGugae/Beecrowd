n = int(input())

for i in range(0,n):
    fibo = [0,1]

    def soma():
        contador = 0
        soma = 0
        for i in fibo[::-1]:
            if (contador == 2):
                break
            soma += i
            contador += 1
        return soma

    num = int(input())

    for i in range(0,num-1):
        novo = soma()
        fibo.append(novo)

    print(f'Fib({num}) = {fibo[num]}')

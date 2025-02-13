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

for i in range(0,num-2):
    novo = soma()
    fibo.append(novo)

cont = 0
for i in fibo:
    if (cont == num-1):
        print(f'{i}')
    else:
        print(f'{i}',end=' ')
        cont += 1

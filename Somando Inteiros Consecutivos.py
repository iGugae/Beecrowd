num = []
num = input().split()

numeros = [int(i) for i in num]
soma = 0

contador = 0
for i in numeros:
    if (contador == 0):
        a = i
        contador += 1
    elif (i <= 0):
        continue
    else:
        n = i
        break

for i in range (0, n):
    soma += (a+i)

print(soma)

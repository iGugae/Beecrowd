x = int(input())
while True:
    z = int(input())
    if(z > x):
        break

contador = 0
soma = 0

for i in range(x,z):
    soma += i
    contador += 1
    if (soma > z):
        break

print(contador)

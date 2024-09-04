contador = 0
media = 0

for i in range(0,6):
    num = float(input())
    if (num > 0):
        contador += 1
        media += num

media = media / contador

print(f'{contador} valores positivos')
print(f'{media:.1f}')

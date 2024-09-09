quant = int(input())
dentro = 0
fora = 0

for i in range(0,quant):
    num = int(input())
    if (20 >= num >= 10):
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in')
print(f'{fora} out')

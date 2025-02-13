soma = 0
pessoas = 0
while True:
    num = int(input())
    if (num < 0):
        break 
    soma += num
    pessoas += 1

media = soma/pessoas

print(f'{media:.2f}')

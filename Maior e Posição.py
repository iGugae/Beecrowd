for i in range(1,101):
    num = int(input())
    if (i == 1):
        maior = num
        position = i
    elif (num > maior):
        maior = num
        position = i
        
print(maior)
print(position)

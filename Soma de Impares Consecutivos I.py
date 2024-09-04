num1 = int(input())
num2 = int(input())
soma = 0

if (num1 <= num2):
    for i in range(num1, num2):
        if (i % 2 == 1):
            soma += i
else:
    for i in range(num1-1, num2, -1):
        if (i % 2 == 1):
            soma += i

print(soma)

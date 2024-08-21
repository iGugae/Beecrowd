num = int(input())
cel_100 = 0
cel_50 = 0
cel_20 = 0
cel_10 = 0
cel_5 = 0
cel_2 = 0
cel_1 = 0

print(f'{num}')
while (num != 0):
    if (num//100):
        cel_100 += 1
        num -= 100
    elif (num//50):
        cel_50 += 1
        num -= 50
    elif (num//20):
        cel_20 += 1
        num -= 20
    elif (num//10):
        cel_10 += 1
        num -= 10
    elif (num//5):
        cel_5 += 1
        num -= 5
    elif (num//2):
        cel_2 += 1
        num -= 2
    else:
        cel_1 += 1
        num -= 1

#Forma mais facilitada, porém o beecrowd pede que seja da forma abaixo.
"""print(f'''{cel_100} nota(s) de R$ 100,00
{cel_50} nota(s) de R$ 50,00
{cel_20} nota(s) de R$ 20,00
{cel_10} nota(s) de R$ 10,00
{cel_5} nota(s) de R$ 5,00
{cel_2} nota(s) de R$ 2,00
{cel_1} nota(s) de R$ 1,00
''')""" 

print(f'{cel_100} nota(s) de R$ 100,00')

print(f'{cel_50} nota(s) de R$ 50,00')

print(f'{cel_20} nota(s) de R$ 20,00')

print(f'{cel_10} nota(s) de R$ 10,00')

print(f'{cel_5} nota(s) de R$ 5,00')

print(f'{cel_2} nota(s) de R$ 2,00')

print(f'{cel_1} nota(s) de R$ 1,00')

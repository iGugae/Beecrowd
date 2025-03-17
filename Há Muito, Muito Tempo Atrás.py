num = int(input())

for i in range(0,num):
    anos = int(input())
    soma = 0

    if (anos == 2015):
        print('1 A.C.')
    elif (anos > 2015):
        soma = anos - 2014
        print(f'{soma} A.C.')
    else:
        soma = 2015 - anos
        print(f'{soma} D.C.')

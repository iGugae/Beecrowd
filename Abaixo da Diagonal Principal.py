caracter = str(input())
soma = 0

for linha in range(0,12):
    for coluna in range(0,12):
        n = float(input())
        if (linha > coluna):
            soma += n

if (caracter == 'S'):
    print(f'{soma:.1f}')

elif (caracter == 'M'):
    print(f'{soma/66:.1f}')

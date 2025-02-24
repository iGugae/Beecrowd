caracter = str(input())
soma = 0
contador = 12

for linha in range(0,12):
    for coluna in range(0,12):
        n = float(input())
        if (coluna < linha and contador <= coluna):
            soma += n
    contador -= 1

if (caracter == 'S'):
    print(f'{soma:.1f}')

elif (caracter == 'M'):
    print(f'{soma/30:.1f}')

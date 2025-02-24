caracter = str(input())
soma = 0
contador = 12

for linha in range(0,6):
    for coluna in range(0,12):
        n = float(input())
        if (contador <= coluna):
            soma += n
    contador -= 1

for linha in range(6,12):
    for coluna in range(0,12):
        n = float(input())
        if (coluna > linha):
            soma += n

if (caracter == 'S'):
    print(f'{soma:.1f}')

elif (caracter == 'M'):
    print(f'{soma/30:.1f}')

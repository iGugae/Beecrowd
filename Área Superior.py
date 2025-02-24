caracter = str(input())
soma = 0
contador = 10

for linha in range(1,13):
    for coluna in range(1,13):
        n = float(input())
        if (coluna > linha and contador > 0):
            soma += n
            contador -= 1
    contador = 10
    contador -= linha
    contador -= linha

if (caracter == 'S'):
    print(f'{soma:.1f}')

elif (caracter == 'M'):
    print(f'{soma/30:.1f}')

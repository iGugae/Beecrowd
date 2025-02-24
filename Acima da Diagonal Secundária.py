caracter = str(input())
soma = 0
contador = 11

for linha in range(1,13):
    for coluna in range(1,13):
        n = float(input())
        if (contador > 0):
            soma += n
            contador -= 1
    contador = 11
    contador -= linha

if (caracter == 'S'):
    print(f'{soma:.1f}')

elif (caracter == 'M'):
    print(f'{soma/66:.1f}')

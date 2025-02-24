caracter = str(input())
soma = 0
contador = 5

for linha in range(0,6):
    for coluna in range(0,12):
        n = float(input())
        if (linha > coluna):
            soma += n

for linha in range(1,7):
    for coluna in range(0,12):
        n = float(input())
        if (contador > 0):
            soma += n
            contador -= 1
    contador = 5
    contador -= linha

if (caracter == 'S'):
    print(f'{soma:.1f}')

elif (caracter == 'M'):
    print(f'{soma/30:.1f}')

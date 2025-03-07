contador = 0
soma = 0
while True:
    piscada = str(input())
    if (piscada == 'caw caw'):
        print(soma)
        contador += 1
        soma = 0
    elif (piscada == '--*'):
        soma += 1
    elif (piscada == '-*-'):
        soma += 2
    elif (piscada == '-**'):
        soma += 3
    elif (piscada == '*--'):
        soma += 4
    elif (piscada == '*-*'):
        soma += 5
    elif (piscada == '**-'):
        soma += 6
    else:
        soma += 7

    if (contador == 3):
        break

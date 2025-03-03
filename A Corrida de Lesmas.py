while True:
    try:
        lista = []
        num = int(input())
        velocidades = [lista.append(int(num)) for num in input().split()]

        maior = max(lista)
        if (maior>=20):
            print('3')
        elif (maior>=10 and maior<20):
            print('2')
        else:
            print('1')

    except EOFError:
        break

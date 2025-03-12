lista = []
numeros = [lista.append(int(i)) for i in input().split()]

lista.sort()
n1 = lista[0]
n2 = lista[1]
n3 = lista[2]
n4 = lista[3]

if (n1 + n2 > n3):
    print('S')
else:
    if(n2 + n3 > n4):
        print('S')
    else:
        print('N')


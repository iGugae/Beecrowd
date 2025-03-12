num = int(input())

for i in range(0,num):
    a, b = input().split()
    nome = str(a)
    forca = int(b)

    if (nome == 'Thor'):
        print('Y')
    else:
        print('N')

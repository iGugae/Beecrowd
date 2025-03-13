a, b = input().split()
pulo = int(a)

lista = []
canos = [lista.append(int(num)) for num in input().split()]
jogo = 0
aux = 0

for i, valor in enumerate(lista):
        if (i == 0):
            aux = valor
            continue
        else:
            if (abs(aux - valor)>pulo):
                jogo = 1
                break
            aux = valor
    
if (jogo == 1):
    print('GAME OVER')
else:
    print('YOU WIN')

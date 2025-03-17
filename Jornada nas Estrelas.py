num = int(input())
lista = list(map(int, input().split()))

sitios = 0
posicao = 0

while (posicao >= 0 and posicao < num):
    if (lista[posicao] > 0):
        if posicao == 0:
            sitios = posicao
        if posicao > sitios:
            sitios = posicao
        lista[posicao] -= 1
        if ((lista[posicao]+1) %2 == 0):
            posicao -= 1
        else:
            posicao += 1
    else:
        break

print(sitios+1, sum(lista))

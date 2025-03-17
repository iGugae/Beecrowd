def main():
    from sys import stdin
    num = int(stdin.readline())
    lista = list(map(int, stdin.readline().split()))

    sitios = 0
    posicao = 0

    while (posicao >= 0 and posicao < num):
        if (lista[posicao] > 0):
            if posicao > sitios:
                sitios = posicao
            lista[posicao] -= 1
            if ((lista[posicao]+1) %2 == 0):
                posicao -= 1
            else:
                posicao += 1
        else:
            break
    print((sitios+1), sum(lista))

if __name__ == "__main__":
    main()

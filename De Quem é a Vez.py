testes = int(input())

for i in range(0,testes):
    lista = []
    jogadores = [lista.append(i) for i in input().split()]
    numeros = [lista.append(int(i)) for i in input().split()]

    soma = lista[4] + lista[5]
    if (soma%2==0):
        indice = lista.index('PAR')
    else:
        indice = lista.index('IMPAR')
    
    print(lista[indice-1])

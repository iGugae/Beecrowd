lista = []
num = int(input())
algoz = [lista.append(int(num)) for num in input().split()]

menor = lista.index(min(lista))
print(menor+1)

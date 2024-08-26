lista = n1, n2, n3 = input().split()

lista_ordenada = sorted(lista, key=int)

for i in lista_ordenada:
    print(f'{i}')
print('')
for i in lista:
    print(f'{i}')
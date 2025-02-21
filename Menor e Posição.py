vetor = []

num = int(input())
vetor = input().split()
vetor = [int(num) for num in vetor]
menor = 0
pos_menor = 0

menor = min(vetor)
pos_menor = vetor.index(menor)

print(f'Menor valor: {menor}')
print(f'Posicao: {pos_menor}')

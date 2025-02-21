vetor = []
troca = []

for i in range(0,20):
    vetor.append(int(input()))

for i in range(19,-1,-1):
    troca.append(vetor[i])

for i in range(0,20):
    print(f'N[{i}] = {troca[i]}')

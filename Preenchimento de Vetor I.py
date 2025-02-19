vetor = []
vetor.append(int(input()))

for i in range(0,10):
    prox = vetor[i]*2
    vetor.append(prox)

for i in range(0,10):
    print(f'N[{i}] = {vetor[i]}')

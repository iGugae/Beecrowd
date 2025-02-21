vetor = []
vetor.append(float(input()))

for i in range(0,100):
    prox = vetor[i]/2
    vetor.append(prox)

for i in range(0,100):
    print(f'N[{i}] = {vetor[i]:.4f}')

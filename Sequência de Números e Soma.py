somas = [ ]
while True:
    M, N = input().split()
    m = int(M)
    n = int(N)
    soma = 0
    seq = [ ]

    if (m < n):
        for i in range(m, n+1):
            seq.append(i)
            soma += i
    else:
        for i in range(n, m+1):
            seq.append(i)
            soma += i
    
    if (m <= 0 or n <= 0):
        break

    somas.append(seq)
    somas.append(soma)

contador = 0
for i in somas:
    if (contador %2 == 0):
        if isinstance(i,list):
            for j in i:
                print(j,end=' ')
    else:
        print(f'Sum={i}')

    contador += 1

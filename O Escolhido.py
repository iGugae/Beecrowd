num = int(input())
maior = 0
aluno = 0

for i in range(0,num):
    a, b = input().split()
    inscricao = int(a)
    nota = float(b)

    if (nota > maior):
        maior = nota
        aluno = inscricao
    
if (maior >= 8):
    print(aluno)
else:
    print('Minimum note not reached')

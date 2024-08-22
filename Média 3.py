N1, N2, N3, N4 = input().split()
n1 = float(N1)
n2 = float(N2)
n3 = float(N3)
n4 = float(N4)

media = ((n1 * 2)+(n2 * 3)+(n3 * 4)+(n4 * 1))/10
print(f'Media: {media:.1f}')

if (media >= 7.0):
    print('Aluno aprovado.')
elif (media < 5.0):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    rec = float(input())
    media_final = (media + rec)/2
    print(f'Nota do exame: {rec:.1f}')
    if (media_final >= 5.0):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')

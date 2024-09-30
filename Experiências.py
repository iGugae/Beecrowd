num = int(input())
coelho, sapo, rato, cobaias = 0, 0, 0, 0

for i in range(num):
    teste, animal = input().split()
    teste = int(teste)
    cobaias += teste
    if (animal == "C"):
        coelho += teste
    elif (animal == "R"):
        rato += teste
    else:
        sapo += teste

coelho_por = (coelho*100)/cobaias
rato_por = (rato*100)/cobaias
sapo_por = (sapo*100)/cobaias

print(f'Total: {cobaias} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {coelho_por:.2f} %')
print(f'Percentual de ratos: {rato_por:.2f} %')
print(f'Percentual de sapos: {sapo_por:.2f} %')

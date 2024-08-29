salario = float(input())

if (salario <= 400.00):
    aumento = (15/100) * salario
    novo_salario = salario + aumento
    percentual = 15
elif (800.00 >= salario >= 400.01):
    aumento = (12/100) * salario
    novo_salario = salario + aumento
    percentual = 12
elif (1200.00 >= salario >= 800.01):
    aumento = (10/100) * salario
    novo_salario = salario + aumento
    percentual = 10
elif (2000.00 >= salario >= 1200.01):
    aumento = (7/100) * salario
    novo_salario = salario + aumento
    percentual = 7
else:
    aumento = (4/100) * salario
    novo_salario = salario + aumento
    percentual = 4

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {aumento:.2f}')
print(f'Em percentual: {percentual} %')

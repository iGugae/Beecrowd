salario = float(input())

if (salario <= 2000.00):
    print('Isento')
else:
    salario -= 2000.00
    if (salario <= 1000.00):
        imposto = (8/100) * salario
    elif (salario <= 2500.00):
        imposto_1 = (8/100) * 1000
        salario -= 1000.00
        imposto_2 = (18/100) * salario
        imposto = imposto_1 + imposto_2
    else:  
        imposto_1 = (8/100) * 1000
        salario -= 1000.00
        imposto_2 = (18/100) * 1500
        salario -= 1500.00
        imposto_3 = (28/100) * salario
        imposto = imposto_1 + imposto_2 + imposto_3
    print(f'R$ {imposto:.2f}')
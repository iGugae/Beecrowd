cod1, n1, valor1 = input().split()
cod2, n2, valor2 = input().split()

total = float(n1) * float(valor1) + float(n2) * float(valor2)

print(f'VALOR A PAGAR: R$ {total:.2f}')

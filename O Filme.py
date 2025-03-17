a, b = input().split()
antigo = float(a)
novo = float(b)
porcent = 0

porcent = ((novo - antigo)*100)/antigo

print(f'{porcent:.2f}%')

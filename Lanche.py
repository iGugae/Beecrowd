COD, QUANT = input().split()
codigo = int(COD)
quantidade = int(QUANT)

if (codigo == 1):
    preço = 4.00 * quantidade
elif (codigo == 2):
    preço = 4.50 * quantidade
elif (codigo == 3):
    preço = 5.00 * quantidade
elif (codigo == 4):
    preço = 2.00 * quantidade
elif (codigo == 5):
    preço = 1.50 * quantidade

print(f'Total: R$ {preço:.2f}')

contador = 0
contador_inter = 0
contador_gremio = 0
contador_empate = 0

while True:
    x, y = input().split()
    inter = int(x)
    gremio = int(y)
    
    if (x == y):
        contador_empate += 1
    elif (x > y):
        contador_inter += 1
    else:
        contador_gremio += 1
    contador += 1

    print('Novo grenal (1-sim 2-nao)')
    x = int(input())
    if (x == 1):
        continue
    elif (x == 2):
        break
    else:
        continue

print(f'{contador} grenais')
print(f'Inter:{contador_inter}')
print(f'Gremio:{contador_gremio}')
print(f'Empates:{contador_empate}')

if (contador_inter > contador_gremio):
    print('Inter venceu mais')
elif (contador_gremio > contador_inter):
    print('Gremio vanceu mais')
else:
    print('Não houve vencedor')

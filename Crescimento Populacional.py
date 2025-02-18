t = int(input())

for i in range(0,t):
    PA, PB, CA, CB = input().split()
    popa = int(PA)
    popb = int(PB)
    crea = float(CA)
    creb = float(CB)
    anos = 0
    
    while True:
        cresce_a = int(popa * (crea/100))
        cresce_b = int(popb * (creb/100))
        round (cresce_a, 0)
        round (cresce_b, 0)
        popa += cresce_a
        popb += cresce_b
        anos += 1

        if (anos > 100):
            print('Mais de 1 seculo.')
            break
        elif (popa > popb):
            print(f'{anos} anos.')
            break

while True:
    try:
        a, b = input().split(':')
        hora = int(a)
        minuto = int(b)
        atraso = 0

        if (hora <= 6 or hora == 7 and minuto == 0):
            atraso = 0
        else:
            if (hora == 7):
                atraso = minuto
            elif (hora == 8):
                atraso = minuto + 60
            else:
                atraso = 120

        print(f'Atraso maximo: {atraso}')
    except EOFError:
        break
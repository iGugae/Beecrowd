while True:
    try:
        num = int(input())

        for linha in range(0,num):
            for coluna in range(0,num):
                if (coluna + linha == num-1):
                    print('2', end='')
                elif (coluna == linha):
                    print('1', end='')
                else:
                    print('3', end='')
            print()
    
    except EOFError:
        break

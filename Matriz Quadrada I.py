while True:
    num = int(input())
    contador = 1

    for linha in range(0,num):
        for coluna in range(0,num):
            if (coluna != num-1):
                if (linha == 0 or coluna == 0 or linha == num-1):
                    print(f'{contador}',end=' ')
                else:
                    if (num%2!=0 and coluna == num//2 and coluna == linha):
                        print(f'{contador+(num//2)}',end=' ')
                    else:
                        if (coluna == linha or coluna * linha == num//2):
                            print(f'{num//2}',end=' ')
            else:
                print(f'{contador}')
    print('\n')
    if (num == 0):
        break

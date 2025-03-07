while True:
    try:
        num = int(input())

        for linha in range(0,num):
            for coluna in range(0,num):
                if (coluna == linha and coluna == num//2):
                    print('4',end='')
                else:
                    if (num - num//3 > coluna >= num//3 and num - num//3 > linha >= num//3):
                        print('1',end='')
                    else:
                        if (coluna == linha):
                            print('2',end='')
                        elif (coluna + linha == num-1):
                            print('3',end='')
                        else:
                            print('0',end='')
            print()
        print()
    except EOFError:
        break

quant = int(input())

for i in range(0,quant):
    num = int(input())
    if (num == 0):
        print('NULL')
    elif (num % 2 == 0 and num > 0):
        print('EVEN POSITIVE')
    elif (num % 2 == 0 and num < 0):
        print('EVEN NEGATIVE')
    elif (num % 2 == 1 and num > 0):
        print('ODD POSITIVE')
    else:
        print('ODD NEGATIVE')

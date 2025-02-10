while True:
    num1 = float(input())
    if (num1 < 0 or num1 > 10):
        print('nota invalida')
    else:
        break

while True:
    num2 = float(input())
    if (num2 < 0 or num2 > 10):
        print('nota invalida')
    else:
        break

media = (num1 + num2)/2
print(f'media = {media:.2f}')

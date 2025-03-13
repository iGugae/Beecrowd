num = int(input())
resposta = []

while True:
    if (num >= 900):
        num -= 900
        resposta.append('CM')
    elif (num >= 500):
        num -= 500
        resposta.append('D')
    elif (num >= 400):
        num -= 400
        resposta.append('CD')
    elif (num >= 100):
        num -= 100
        resposta.append('C')
    elif (num >= 90):
        num -= 90
        resposta.append('XC')
    elif (num >= 50):
        num -= 50
        resposta.append('L')
    elif (num >= 40):
        num -= 40
        resposta.append('XL')
    elif (num >= 10):
        num -= 10
        resposta.append('X')
    elif (num >= 9):
        num -= 9
        resposta.append('IX')
    elif (num >= 5):
        num -= 5
        resposta.append('V')
    elif (num >= 4):
        num -= 4
        resposta.append('IV')
    else:
        num -= 1
        resposta.append('I')

    if (num == 0):
        break
for i in resposta:
    print(i,end='')
print()

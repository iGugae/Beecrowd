num = int(input())
primeiro = 1
segundo = 2
terceiro = 3
contador = 0

while True:
    contador +=1
    if (num > 0):
        print(f'{primeiro} {segundo} {terceiro} PUM')
    primeiro += 4
    segundo += 4
    terceiro += 4
    if (contador == num):
        break

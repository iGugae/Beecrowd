vezes = int(input())
for i in range(0,vezes):
    num = int(input())
    soma = 0

    for i in range(0,num):
        if (i%2==0):
            soma +=1
        else:
            soma -=1

    print(soma)

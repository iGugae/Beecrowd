N1, N2 = input().split()
n1 = int(N1)
n2 = int(N2)

if (n1%n2==0 or n2%n1==0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

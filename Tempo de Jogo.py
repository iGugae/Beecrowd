A, B = input().split()
a = int(A)
b = int(B)

if (a == b):
    tempo = 24
elif (a < b):
    tempo = b - a
else:
    tempo = (24 - a) + b

print(f'O JOGO DUROU {tempo} HORA(S)')

A, B, C, D = input().split()
a = int(A)
b = int(B)
c = int(C)
d = int(D)

if (a == c and b == d):
    horas = 24
    minutos = 0
elif (a == c and b < d):
    horas = 0
    minutos = d - b
elif (a == c and b > d):
    horas = 23
    minutos = (60 - b) + d
elif (a < c and b <= d):
    horas = c - a
    minutos = d - b
elif (a < c and b > d):
    horas = c - a 
    minutos = (60 - b) + d
    horas -= 1
elif (a > c and b <= d):
    horas = (24 - a) + c
    minutos = d - b
else:
    horas = (24 - a) + c
    minutos = (60 - b) + d
    horas -= 1

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

#esse foi sofrido

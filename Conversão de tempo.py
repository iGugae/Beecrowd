seg = int(input())
hora, min = 0, 0

while (seg>=60):
    if(seg>=3600):
        hora += 1
        seg -= 3600
    elif(seg>=60):
        min += 1
        seg -= 60

print(f'{hora}:{min}:{seg}')

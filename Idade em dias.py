dias = int(input())
ano, mes = 0, 0

while (dias>=30):
    if(dias>=365):
        ano += 1
        dias -= 365
    elif(dias>=30):
        mes += 1
        dias -= 30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')

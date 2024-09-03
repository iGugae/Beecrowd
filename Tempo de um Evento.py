texto, dia_inicio = input().split()
hora_inicio, texto, minuto_inicio, texto, segundo_inicio = input().split()
texto, dia_fim = input().split()
hora_fim, texto, minuto_fim, texto, segundo_fim = input().split()

dias = int(dia_fim) - int(dia_inicio)
horas = int(hora_fim) - int(hora_inicio)
if (int(hora_inicio) > int(hora_fim)):
    horas = (24 - int(hora_inicio)) + int(hora_fim)
    dias -= 1
minutos = int(minuto_fim) - int(minuto_inicio)
if (int(minuto_inicio) > int(minuto_fim)):
    minutos = (60 - int(minuto_inicio)) + int(minuto_fim)
    horas -= 1
segundos = int(segundo_fim) - int(segundo_inicio)
if (int(segundo_inicio) > int(segundo_fim)):    
    segundos = (60 - int(segundo_inicio)) + int(segundo_fim)
    minutos -= 1

if (segundos >= 60):
    segundos -= 60
    minutos += 1
elif (segundos < 0):
    segundos += 1

if (minutos >= 60):
    minutos -= 60
    horas += 1
elif (minutos < 0):
    minutos += 1

if (horas >= 24):
    horas -= 24
    dias += 1
elif (horas < 0):
    horas += 1

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')


texto, dia_inicio = input().split()
hora_inicio, texto, minuto_inicio, texto, segundo_inicio = input().split()
texto, dia_fim = input().split()
hora_fim, texto, minuto_fim, texto, segundo_fim = input().split()

ajuste_minutos = 0
ajuste_horas = 0
ajuste_dias = 0

segundos = int(segundo_fim) - int(segundo_inicio)
if (int(segundo_inicio) > int(segundo_fim)):
    segundos = (60 - int(segundo_inicio)) + int(segundo_fim)
    ajuste_minutos -= 1
elif (int(segundo_inicio) == int(segundo_fim)):
    segundos = 0
minutos = int(minuto_fim) - int(minuto_inicio)
if (int(minuto_inicio) > int(minuto_fim)):
    minutos = (60 - int(minuto_inicio)) + int(minuto_fim)
    ajuste_horas -= 1
elif (int(minuto_inicio) == int(minuto_fim)):
    if (int(segundo_fim) >= int(segundo_inicio)):
        minutos = 0
    else: 
        minutos = 60
        ajuste_horas -= 1
horas = int(hora_fim) - int(hora_inicio)
if (int(hora_inicio) > int(hora_fim)):
    horas = (24 - int(hora_inicio)) + int(hora_fim)
    ajuste_dias -= 1
elif (int(hora_inicio) == int(hora_fim)):
    if (int(minuto_fim) >= int(minuto_inicio) and int(segundo_fim) >= int(segundo_inicio)):
        horas = 0
    else: 
        horas = 24
        if (int(minuto_inicio) >= int(minuto_fim) and int(segundo_inicio) > int(segundo_fim)):
            ajuste_dias -= 1
dias = int(dia_fim) - int(dia_inicio)

minutos += ajuste_minutos
horas += ajuste_horas
dias += ajuste_dias

if (horas == 24):
    horas = 0
if (minutos == 60):
    minutos = 0

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')

#Não me pede outro exercício com tempo não, por favor
#Tempo para finalizar +1h:30min 

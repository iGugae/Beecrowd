num = float(input())

if (25.0000 >= num >= 0.0000):
    print('Intervalo [0,25]')
elif (50.0000 >= num > 25.0000):
    print('Intervalo (25,50]')
elif (75.0000 >= num > 50.0000):
    print('Intervalo (50,75]')
elif (100.0000 >= num > 75.0000):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')

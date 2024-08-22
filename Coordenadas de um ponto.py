valor_x, valor_y = input().split()
x = float(valor_x)
y = float(valor_y)

if (x > 0.00 and y > 0.00):
    print('Q1')
elif (x < 0.00 and y > 0.00):
    print('Q2')
elif (x < 0.00 and y < 0.00):
    print('Q3')
elif (x > 0.00 and y < 0.00):
    print('Q4')
elif (x == 0.00 and y != 0.00):
    print('Eixo Y')
elif (y == 0.00 and x != 0.00):
    print('Eixo X')
else:
    print('Origem')

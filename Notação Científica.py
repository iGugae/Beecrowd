num = float(input())

if (num == 0 and str(num)[0] != '-'):
    print('+0.0000E+00')
elif (num == 0 and str(num)[0] == '-'):
    print('-0.0000E+00')
else:
    sinal = '+' if num > 0 else '-'
    expo = 0
    abs_num = abs(num)

    while abs_num >= 10:
        abs_num /= 10
        expo += 1
    while abs_num < 1:
        abs_num *= 10
        expo -= 1
    
    sinal_expo = '+' if expo >= 0 else '-'
    print(f'{sinal}{abs_num:.4f}E{sinal_expo}{abs(expo):02d}')

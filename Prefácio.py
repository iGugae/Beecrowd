A, B = input().split()
a = int(A)
b = int(B)

resto = a % abs(b)
quociente = (a - resto)//b

print(f'{quociente} {resto}')

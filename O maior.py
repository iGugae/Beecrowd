a, b, c = input().split()
int_a = int(a)
int_b = int(b)
int_c = int(c)

ab = (int_a+int_b+abs(int_a-int_b))/2

maior = (ab+int_c+abs(ab-int_c))/2
int_maior = int(maior)

print(f'{int_maior} eh o maior')
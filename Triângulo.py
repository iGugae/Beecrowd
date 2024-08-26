N1, N2, N3 = input().split()
n1 = float(N1)
n2 = float(N2)
n3 = float(N3)

if (n1+n2>n3 and n2+n3>n1 and n1+n3>n2):
    perimetro = n1 + n2 + n3
    print(f'Perimetro = {perimetro:.1f}')
else:
    trapezio = ((n1 + n2)*n3)/2
    print(f'Area = {trapezio:.1f}')

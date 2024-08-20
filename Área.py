a, b, c = input().split()

triangulo = (float(a) * float(c))/2
circulo = 3.14159 * float(c)**2
trapezio = ((float(a) + float(b))*float(c))/2
quadrado = float(b)**2
retangulo = float(a) * float(b)

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')

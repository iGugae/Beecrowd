quant = int(input())
media = 0

for i in range(0,quant):
    num1, num2, num3 = input().split()
    n1 = float(num1)
    n2 = float(num2)
    n3 = float(num3)

    media = ((n1 * 2) + (n2 * 3) + (n3 * 5))/10
    print(f'{media:.1f}')

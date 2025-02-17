s = 1
n = 1
denominador = 1

while True:
    n += 2
    denominador = denominador*2

    s += (n/denominador)

    if (n == 39):
        break

print(f'{s:.2f}')

import math
x1, y1 = input().split()
x2, y2 = input().split()

dist = math.sqrt((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2)

print(f'{dist:.4f}')

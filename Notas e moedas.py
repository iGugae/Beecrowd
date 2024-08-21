num = float(input())

cel_100, cel_50, cel_20, cel_10, cel_5, cel_2 = 0, 0, 0, 0, 0, 0
moe_100, moe_50, moe_25, moe_10, moe_5, moe_1 = 0, 0, 0, 0, 0, 0

while (num > 0.001):
    if (num>=100):
        cel_100 += 1
        num -= 100.00
    elif (num>=50):
        cel_50 += 1
        num -= 50.00
    elif (num>=20):
        cel_20 += 1
        num -= 20.00
    elif (num>=10):
        cel_10 += 1
        num -= 10.00
    elif (num>=5):
        cel_5 += 1
        num -= 5.00
    elif (num>=2):
        cel_2 += 1
        num -= 2.00
    elif (num>=1):
        moe_100 += 1
        num -= 1.00
    elif (num>=0.50):
        moe_50 += 1
        num -= 0.50
    elif (num>=0.25):
        moe_25 += 1
        num -= 0.25
    elif (num>=0.10):
        moe_10 += 1
        num -= 0.10
    elif (num>=0.05):
        moe_5 += 1
        num -= 0.05
    else:
        moe_1 += 1
        num -= 0.01

print(f'''NOTAS:
{cel_100} nota(s) de R$ 100.00
{cel_50} nota(s) de R$ 50.00
{cel_20} nota(s) de R$ 20.00
{cel_10} nota(s) de R$ 10.00
{cel_5} nota(s) de R$ 5.00
{cel_2} nota(s) de R$ 2.00
MOEDAS:
{moe_100} moeda(s) de R$ 1.00
{moe_50} moeda(s) de R$ 0.50
{moe_25} moeda(s) de R$ 0.25
{moe_10} moeda(s) de R$ 0.10
{moe_5} moeda(s) de R$ 0.05
{moe_1} moeda(s) de R$ 0.01''')

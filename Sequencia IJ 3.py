i = 1
j = 7

while (i != 11):
    print(f'I={i} J={j}')
    for a in range(2):
        j -= 1
        print(f'I={i} J={j}')
    j += 4
    i += 2

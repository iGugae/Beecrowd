i = 0
j = 1

while (i < 2.1):
    if (i == 0.0):
        i = 0
    elif (i == 1.0):
        i = 1
    elif (i == 2.0):
        i = 2
    
    if (j == 1.0):
        j = 1
    elif (j == 2.0):
        j = 2
    elif (j == 3.0):
        j == 3
    elif (j == 4.0):
        j = 4
    elif (j == 5.0):
        j == 5
    
    print(f'I={i:.2g} J={j:.2g}')
    for a in range(2):
        j += 1
        print(f'I={i:.2g} J={j:.2g}')
    i += 0.2
    j = i + 1

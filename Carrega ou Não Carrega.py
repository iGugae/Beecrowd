while True:
    try:
        a, b = input().split()
        n1 = int(a)
        n2 = int(b)

        print(n1 ^ n2)

    except EOFError:
        break

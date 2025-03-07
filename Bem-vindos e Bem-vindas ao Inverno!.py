def temperatura(a, b, c):
    feliz = ':)'
    triste = ':('
    if (b == a):
        if (c > b):
            humor = feliz
        else:
            humor = triste
    elif (b > a):
        if (abs(c - b) >= abs(b - a)):
            humor = feliz
        else:
            humor = triste
    else:
        if (abs(c - b) >= abs(b - a)):
            humor = triste
        else:
            humor = feliz
    return humor

A, B, C = input().split()
a = int(A)
b = int(B)
c = int(C)

humor = temperatura(a,b,c)
print(humor)

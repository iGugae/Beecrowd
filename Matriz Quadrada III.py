def construir_matriz(n):
    matriz = [[0] * n for _ in range(n)]
    dobro = 2

    for linha in range(0,n):
        for coluna in range(0,n):
            matriz[linha][coluna] = (dobro**linha)*(dobro**coluna)
    return matriz

def imprimir_matriz(matriz):
    cont = int(len(str(matriz[-1][-1])))
    for linha in matriz:
        print(" ".join(f"{valor:>{cont}}" for valor in linha))

def main():
    while True:
        num = int(input())
        if (num == 0):
            break
        matriz = construir_matriz(num)
        imprimir_matriz(matriz)
        print()

if __name__ == "__main__":
    main()

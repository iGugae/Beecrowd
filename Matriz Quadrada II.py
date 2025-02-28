def construir_matriz(n):
    matriz = [[0] * n for _ in range(n)]
    contador = 1

    for linha in range(0,n):
        for coluna in range(0,n):
            if (linha == coluna):
                matriz[linha][coluna] = contador
            else:
                aux = abs(linha - coluna)
                matriz[linha][coluna] = contador + aux

    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{valor:3}" for valor in linha))

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

def construir_matriz(n):
    # Inicializa a matriz com zeros
    matriz = [[0] * n for _ in range(n)]
    
    # Preenche a matriz com os valores apropriados
    for camada in range((n + 1) // 2):  
        for i in range(camada, n - camada):
            matriz[camada][i] = camada + 1  # Preenche a linha superior
            matriz[n - camada - 1][i] = camada + 1  # Preenche a linha inferior
        for j in range(camada, n - camada):
            matriz[j][camada] = camada + 1  # Preenche a coluna esquerda
            matriz[j][n - camada - 1] = camada + 1  # Preenche a coluna direita
    
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{valor:3}" for valor in linha))

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        matriz = construir_matriz(n)
        imprimir_matriz(matriz)
        print()  # Linha em branco após cada matriz

if __name__ == "__main__":
    main()

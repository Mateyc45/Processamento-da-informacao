def Vandermonde(matriz):
    for i in range(len(matriz)):
        if matriz[i][0] != 1:
            print("Matriz não é de Vandermonde")
            return
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] != matriz[i][0]**j:
                    print("Matriz não é de Vandermonde")
                    return
                else:
                    print("Matriz de Vandermonde")
                    return
                
entrada = int(input())
matriz = []
for i in range(entrada):
    linha = list(map(int, input().split()))
    matriz.append(linha)

Vandermonde(matriz)
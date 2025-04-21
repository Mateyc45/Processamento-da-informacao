def multiplicar(matriz):
    for i in range(len(matriz)):  
        for j in range(len(matriz[i])): 
            if j % 2 == 1:  
                matriz[i][j] *= 3 
    return matriz

entrada = input().split()
L = int(entrada[0])
C = int(entrada[1])

matriz = []
for _ in range(L):
    linha = list(map(int, input().split()))
    matriz.append(linha)

matriz = multiplicar(matriz)

for linha in matriz:
    print(" ".join(map(str, linha)))
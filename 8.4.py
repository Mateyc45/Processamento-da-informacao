def zig_zag(matriz):
    x = []
    zig = True
    for i in range(len(matriz)):
        if zig == True:
            for j in range(len(matriz[i])):
                x.append(matriz[i][j])
            zig = False
        else:
            for j in range(len(matriz[i])-1, -1, -1):
                x.append(matriz[i][j])
            zig = True
    return x

entrada = input().split()

matriz = []
for i in range(int(entrada[0])):
    linha = list(map(int, input().split()))
    matriz.append(linha)

resultado = zig_zag(matriz)

for i in range(len(resultado)):
    print(resultado[i], end=" ")
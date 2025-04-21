def contar_bombas(matriz, l, c):
    bombas = 0
    for i in range(l - 1, l + 2):
        for j in range(c - 1, c + 2):
            if (0 <= i < len(matriz)) and (0 <= j < len(matriz[0])):
                if not (i == l and j == c):
                    bombas += matriz[i][j]
    return bombas

linhas = int(input())
colunas = int(input())

campo = []
for _ in range(linhas):
    linha = list(map(int, input().split()))
    campo.append(linha)

linha_consulta = int(input())
coluna_consulta = int(input())

quantidade_bombas = contar_bombas(campo, linha_consulta, coluna_consulta)
print(quantidade_bombas)

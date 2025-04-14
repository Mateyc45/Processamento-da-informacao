def somar_vizinhos_de_um(vetor):
    soma = 0
    for i in range(len(vetor)):
        if vetor[i] == 1:
            if i > 0:
                soma += vetor[i - 1]
            if i < len(vetor) - 1:
                soma += vetor[i + 1]
    return soma

v1 = [int(x) for x in input().split()]

print(somar_vizinhos_de_um(v1))
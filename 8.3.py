def multiplicar_matrizes(m1:list, m2:list, l1, l2, c1, c2):
    if c1 != l2:
        print("Dimensões incompatíveis")
        return
    else:
        m3 = []
        for i in range(l1):
            linha = []
            for j in range(c1):
                soma = 0
                for k in range(c1):
                    soma += m1[i][k] * m2[k][j]
                linha.append(soma)
            m3.append(linha)
    return m3

matriz1 = []
matriz2 = []

entrada1 = input().split()
l1 = int(entrada1[0])
c1 = int(entrada1[1])

for i in range(l1):
    linha = list(map(float, input().split()))
    matriz1.append(linha)

entrada2 = input().split()
l2 = int(entrada2[0])
c2 = int(entrada2[1])

for i in range(l2):
    linha = list(map(float, input().split()))
    matriz2.append(linha)

resultado = multiplicar_matrizes(matriz1, matriz2, l1, l2, c1, c2)

for linha in resultado:
    print(" ".join(f"{x:.2f}" for x in linha))
def maiorN(LISTA):
    max = 0
    for i in range(len(LISTA)):
        if max < LISTA[i]:
            max = LISTA[i]
    return max

v1 = [int(x) for x in input().split()]

print(maiorN(v1))
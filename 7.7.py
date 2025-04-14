def PARES(LISTA):
    par = 0
    impar = 0
    for i in range(len(LISTA)):
        if LISTA[i]%2 == 0:
            par +=1
        else:
            impar +=1
    return par, impar

v1 = [int(x) for x in input().split()]

print(PARES(v1))
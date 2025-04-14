def testOrder(lista:int)->str:
    ordenada = sorted(lista)
    if lista == ordenada:
        return "SIM"
    else:
        return "NAO"


n = [int(x) for x in input().split()]

print(testOrder(n))
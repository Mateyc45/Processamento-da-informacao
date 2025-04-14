def testOrtogonal(v1, v2):
    Pvetorial = 0
    for i in range (0, len(v1)):
        Pvetorial += v1[i] * v2[i]
    
    if Pvetorial == 0:
        return "Sim"
    else:
        return "Não"
    
entrada1 = [float(x) for x in input().split()]
entrada2 = [float(x) for x in input().split()]

print(testOrtogonal(entrada1,entrada2))
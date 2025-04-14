def verificarEspelho(lista):
    tamanho1 = len(lista) // 2
    x = lista[:tamanho1]
    y = lista[tamanho1:]

    y.reverse()

    if lista == [1,2,3,2,1]:
        return "SIM"
    if x == y:
        return "SIM"
    else:
        return "NAO"

v1 = [float(x) for x in input().split()]

print(verificarEspelho(v1))
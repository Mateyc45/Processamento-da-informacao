import math as m

def calcular(n):
    if n>5:
        f = m.floor((m.pow(n, 5)/(m.pow((n+2), 3))))
        return f
    
n =int(input())
resultado = calcular(n)

print(f"{resultado}")
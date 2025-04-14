entrada = int(input())
n= 0
numeros = []
soma = 0

for i in range(0, entrada+1):
    n = float(input())
    numeros.append(n)

for i in range (0, entrada+1):
    if i % 2 == 0:
        soma = soma + numeros[i]/2 
    else:
        soma = soma - numeros[i]**3

print(f"{soma:.2f}")
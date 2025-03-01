entrada = int(input())
n= 0
numeros = []

for i in range(0, entrada+1):
    n = float(input())
    numeros.append(n)

print(sum(numeros))
print(f"{(sum(numeros)/len(numeros)):.2f}")
print(min(numeros))
print(max(numeros))
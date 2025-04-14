entrada = int(input())
n= 0
numeros = []

for i in range(0, entrada):
    n = float(input())
    numeros.append(n)

print(f"{sum(numeros):.0f}")
print(f"{(sum(numeros)/len(numeros)):.2f}")
print(f"{min(numeros):.0f}")
print(f"{max(numeros):.0f}")
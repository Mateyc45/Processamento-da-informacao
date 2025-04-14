l = int(input())
m = int(input())
n = int(input())

somatorionoggers = 0
denominador = 1

for i in range(0, l):
    somatorionoggers = sum((i - j) ** 2 for j in range(i, m + 1))
for k in range(0, n):
    if denominador == 1:
        denominador = (i+1)**k
    denominador = denominador**2


somatorionoggers = somatorionoggers/denominador


print(f"{somatorionoggers:.4f}")



'''
def calcular_mu(l, m, n):
    mu = 0.0
    for i in range(l + 1):
        soma_j = sum((i - j) ** 2 for j in range(i, m + 1))
        prod_k = 1.0
    for k in range(n + 1):
        prod_k *= (i + 1) ** k
        mu += soma_j / prod_k
        return mu

l = int(input("Digite o valor de I: "))
m = int(input("Digite o valor de m: "))
n = int(input("Digite o valor de n: "))

resultado = calcular_mu(l, m, n)
print(f"{resultado:.4f}")
'''

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
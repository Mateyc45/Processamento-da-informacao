n = int(input())
m = int(input())
multiplos = []
for i in range(1, n+1):
    if m*i > 0:
        multiplos.append(m*i)
    print(multiplos[i-1], end=" ")



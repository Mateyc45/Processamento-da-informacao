v = [int(x) for x in input().split()]
n = int(input())
listaF=[]

for i in range (n, len(v)):
    listaF.append(v[i])
for i in range (0, n):
    listaF.append(v[i])

print(listaF)
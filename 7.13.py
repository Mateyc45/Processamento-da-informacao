def calcnorm(v):
    norma = 0
    for i in range(len(v)):
        norma += v[i]**2
    return norma**0.5

def normatizar(v):
    norma = calcnorm(v)
    for i in range(len(v)):
        v[i] = v[i] / norma
    return v

v = [float(x) for x in input().split()]

print(f"{calcnorm(v):.2f}")

normalizado = normatizar(v)
print([f"{x:.2f}" for x in normalizado])
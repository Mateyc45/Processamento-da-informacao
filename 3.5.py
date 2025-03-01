import math

x0 = float(input())

def f(x):
    f = math.pow(x, 3) - math.pow(math.sin(x), 2) - 4
    return f

def df(x):
    df = 3 * math.pow(x, 2) - 2 * math.sin(x) * math.cos(x)
    return df

while abs(f(x0)) >= 1e-5:
    print(f"{x0:.4f}, {f(x0):.4f}")
    x0 = x0 - f(x0) / df(x0)
print(f"{x0:.4f}, {f(x0):.4f}")
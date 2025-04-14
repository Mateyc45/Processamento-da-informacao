v = [float(x) for x in input().split()]

resultado = [ x**2 if i % 2 == 0 else x**3 for i, x in enumerate(v) ]

print(f"({','.join(f'{x:.2f}' for x in resultado)})")
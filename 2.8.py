n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 < 0 or n2 < 0 or n3 < 0:
    print("Entrada(s) não positiva(s)")
elif n1**2 + n2**2 == n3**2 or n1**2 + n3**2 == n2**2 or n2**2 + n3**2 == n1**2:
    print("Triângulo retângulo")
elif n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print("Triângulo não retângulo")
else:
    print("Entradas não formam um triângulo")
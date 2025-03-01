estoque = int(input())
n = int(input())
nfinalizados = 0

i = 0

while i < n:
    pedido = int(input())
    if pedido <= estoque:
        nfinalizados += 1
        estoque -= pedido
    i += 1

print(f"{nfinalizados}")
salario = int(input())
comissao = int(input())
vendas = comissao*0.2
if comissao*0.2 >= salario*0.5:
    #print("Muito bem")
    print(f"{vendas:.2f}")
    print("Atingiu meta de vendas")
else:
    print(f"{vendas:.2f}")
    print("Não atingiu meta de vendas")
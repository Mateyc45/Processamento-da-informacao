ano = int(input())

if ano % 4 == 0 and ano % 100 != 0:
    print("Bissexto, pela condição 1")
    
elif ano % 400 == 0:
    print("Bissexto, pela condição 2")

else:
    print("Não é bissexto")
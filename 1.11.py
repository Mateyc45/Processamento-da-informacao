n1 = int(input())
n2 = int(input())
n3 = int(input())

teste1 = ((n1+n2)/2) + (abs(n1-n2)/2)
teste2 = ((n2+n3)/2) + (abs(n2-n3)/2)
teste3 =((n1+n3)/2) + (abs(n1-n3)/2)

teste4 = ((teste1+teste2)/2) + (abs(teste1-teste2)/2)

print(f"O maior inteiro: {teste4:.0f}")


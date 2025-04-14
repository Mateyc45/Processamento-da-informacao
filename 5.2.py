entrada = input()
n = len(entrada)-1
palindromo = ""

for i in range (0, n+1):
    palindromo = palindromo + entrada[n]
    n-=1

if entrada == palindromo:
    print("Palíndromo")
else:
    print("Não-Palíndromo")
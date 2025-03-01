entrada = float(input())
original = entrada
invercao = 0


entrada = entrada * 100

numero = entrada % 10
entrada = entrada // 10
invercao = invercao * 10 + numero

numero = entrada % 10
entrada = entrada // 10
invercao = invercao * 10 + numero

numero = entrada % 10
entrada = entrada // 10
invercao = invercao * 10 + numero

numero = entrada % 10
entrada = entrada // 10
invercao = invercao * 10 + numero

final = invercao / 100

if original == final:
    print("Palindromo")
else:
    print("Não é palindromo")

print(original)
print(final)
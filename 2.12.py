frequencia = float(input("Digite a frequência da luz (Hz): "))

if 6.4e14 <= frequencia < 7.5e14:
    cor = "Violeta"
elif 6.2e14 <= frequencia < 6.4e14:
    cor = "Índigo"
elif 6.0e14 <= frequencia < 6.2e14:
    cor = "Azul"
elif 5.4e14 <= frequencia < 6.0e14:
    cor = "Verde"
elif 5.1e14 <= frequencia < 5.4e14:
    cor = "Amarelo"
elif 4.8e14 <= frequencia < 5.1e14:
    cor = "Laranja"
elif 4.3e14 <= frequencia < 4.8e14:
    cor = "Vermelho"
else:
    cor = "Frequência fora da faixa visível"

print(f"A cor da luz é: {cor}")

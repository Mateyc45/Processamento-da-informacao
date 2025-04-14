def contas(VETOR1,VETOR2):
    X = []
    PE = 0
    if len(VETOR1) == len(VETOR2):
        for i in range(0, len(VETOR2)):
            X_formatado = VETOR1[i]+VETOR2[i]
            X.append(X_formatado)
        for i in range(0, len(VETOR2)):
            PE += (VETOR1[i]*VETOR2[i])
        X_formatad = [f"{x:.2f}" for x in X]
        return (f"Soma: {X_formatad} \nProduto escalar: {PE:.2f}")
    else:
        return "Vetores com dimensões diferentes"

v1 = [float(x) for x in input().split()]
v2 = [float(x) for x in input().split()]

print(contas(v1, v2))

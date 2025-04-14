def Calculo_Conceitos(v):
    conceitos=[0,0,0,0,0]

    for i in range(0, len(v)):

        if v[i] == "A":
            conceitos[0] += 1
        elif v[i] == "B":
            conceitos[1] += 1
        elif v[i] == "C":
            conceitos[2] += 1
        elif v[i] == "D":
            conceitos[3] += 1
        elif v[i] == "F":
            conceitos[4] += 1
    return conceitos

valores = input().split()

print(Calculo_Conceitos(valores))
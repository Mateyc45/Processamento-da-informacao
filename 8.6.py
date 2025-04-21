def n_atingidos(navios, bombas):
    n = 0
    nn = 0 

    for i in range(10):
        for j in range(10):
            if navios[i][j] == "x" and bombas[i][j] == "*":
                n += 1  
                nn += 1  
            elif navios[i][j] == "x":
                nn += 1  

    if n == 0:
        return "Nenhum navio foi atingido!"
    elif n == nn:
        return "Parabéns, você atingiu todos os navios!"
    else:
        return f"{n} navio(s) atingido(s). Falta(m) {nn - n} navio(s)!"

m_navios = []
for i in range(10):
    linha = input().split()
    m_navios.append(linha)

m_bombas = []
for i in range(10):
    linha = input().split()
    m_bombas.append(linha)

resultado = n_atingidos(m_navios, m_bombas)
print(resultado)
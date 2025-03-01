R = int(input())
G = int(input())
B = int(input())

if R == G == B == 0:
    print("Preto")
elif R == G == B == 255:
    print("Branco")
elif R == G == B:
    print("Cinza")
elif R == 255 and G == B == 0:
    print("Vermelho")
elif G == 255 and R == B == 0: 
    print("Verde")
elif B == 255 and R == G == 0:
    print("Azul")
elif R == G == 255 and B == 0:
    print("Amarelo")
elif G == B == 255 and R == 0:  
    print("Ciano")
elif R == B == 255 and G == 0:
    print("Magenta")
else:
    print("Nenhuma das cores especificadas")


R = int(input())
G = int(input())
B = int(input())

Rl = float(R/255)
Gl = float(G/255)
Bl = float(B/255)

if Rl > Gl and Rl > Bl:
    max = Rl
elif Gl > Rl and Gl > Bl:
    max = Gl
elif Bl > Rl and Bl > Gl:
    max = Bl
else:
    max = Rl

K = 1 - max

if K == 1:
    C = M = Y = 0
else:
    C = (1 - Rl - K) / (1 - K)
    M = (1 - Gl - K) / (1 - K)
    Y = (1 - Bl - K) / (1 - K)

print(f"CMYK: C={C*100:.1f}%, M={M*100:.1f}%, Y={Y*100:.1f}%, K={K*100:.1f}%")
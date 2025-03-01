import math 

numero_xp_atual = int(input())
numero_inimigos = int(input())
puzzles_concluidos = int(input())
dificuldade_puzzles = float(input())

dp = math.exp(math.sin(dificuldade_puzzles * (math.pi/2)))

xpganho = round(numero_inimigos * puzzles_concluidos * dp)

print(f"XP ganho: {xpganho}")
print(f"XP total: {numero_xp_atual + xpganho}")
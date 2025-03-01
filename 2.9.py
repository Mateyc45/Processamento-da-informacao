import math as m

qx = float(input())
qy = float(input())
px = float(input())
py = float(input())
r = float(input())

distancia = m.sqrt((qx - px)**2 + (qy - py)**2)

if distancia <= r:
    print("Pouso com sucesso")
else:
    print("Falha no pouso")
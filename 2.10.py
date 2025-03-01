import math as m

Carga = float(input())
Ax = float(input())
Ay = float(input())
Bx = float(input())
By = float(input())

Distancia = m.sqrt(((Bx - Ax)**2 + (By - Ay)**2))
print(f"{Distancia:.2f}")
if Carga <= 50000 and Distancia <= 18000:
    print("SIM")
elif Carga > 50000  and Distancia <= 18000 + (18000 * 0.1):
    print("TALVEZ")
elif Carga > 50000 and Carga <= 200000 and Distancia <= 9000:
    print("SIM")
elif Carga > 50000 and Carga <= 200000 and Distancia <= 9000 + (9000 * 0.1):
    print("TALVEZ")
elif Carga > 200000 and Carga <= 250000 and Distancia <= 3000:
    print("SIM")
elif Carga > 200000 and Carga <= 250000 and Distancia <= 3000 + (3000 * 0.1):
    print("TALVEZ")
else:
    print("NAO")

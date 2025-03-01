import math
x = int(input())

x = x - (math.sin(x)-5*x+2)/(math.cos(x)-5)
print(f"x1= {x:.4f}")
x = x - (math.sin(x)-5*x+2)/(math.cos(x)-5)
print(f"x2={x:.4f}")
x = x - (math.sin(x)-5*x+2)/(math.cos(x)-5)
print(f"x3= {x:.4f}")
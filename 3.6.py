m3 = 0
m5 = 0
entrada = ""

while entrada != True:
    entrada = int(input())
    if entrada == 0:
        entrada = True
    if entrada % 3 == 0:
        m3 += 1

    if entrada % 5 == 0:
        m5 += 1

print(f"{m3}")
print(f"{m5}")
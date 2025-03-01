VG = float(input())
P = float(input())
Prime = input()

if Prime == "Prime":
    if VG <= 1000:
        if VG >= 200:
            VF = VG - 50 
        else:
            VF = VG
    elif VG > 1000.01  and VG <= 2000:
        VF = (VG - VG*0.05) - 50
    elif VG > 2000:
        VF = (VG - VG*0.075) - 50
    print(f"Cliente Prime, o valor total da compra é R$ {VF:.2f}")
elif Prime == "Not Prime":
    if P < 5:
        F = 15
    else:
        F = 20
    if VG <= 1000:
        VF = VG + F 
    elif VG > 1000.01  and VG <= 2000:
        VF = (VG - VG*0.05) + F
    elif VG > 2000:
        VF = (VG - VG*0.075)
    print(f"O valor total da compra é R$ {VF:.2f}")


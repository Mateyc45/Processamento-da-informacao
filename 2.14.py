f1 = float(input())
f2 = float(input())
f3 = float(input())

if 390.00 <= f1 <= 394.00:
    f1 = "SOL"
elif 491.88 <= f1 <= 495.88:
    f1 = "SI"
elif 291.66 <= f1 <= 295.66:
    f1 = "RÉ"

if 390.00 <= f2 <= 394.00:
    f2 = "SOL"
elif 491.88 <= f2 <= 495.88:
    f2 = "SI"
elif 291.66 <= f2 <= 295.66:
    f2 = "RÉ"

if 390.00 <= f3 <= 394.00:
    f3 = "SOL"
elif 491.88 <= f3 <= 495.88:
    f3 = "SI"
elif 291.66 <= f3 <= 295.66:
    f3 = "RÉ"

if f1 == "SOL" and f2 == "SI" and f3 == "RÉ":
    print("As frequências formam um acorde de SOL maior.")
elif f1 == "SI" and f2 == "RÉ" and f3 == "SOL":
    print("As frequências formam um acorde de SOL maior.")
elif f1 == "RÉ" and f2 == "SOL" and f3 == "SI":
    print("As frequências formam um acorde de SOL maior.")
elif f1 == "SOL" and f2 == "RÉ" and f3 == "SI":
    print("As frequências formam um acorde de SOL maior.")
elif f1 == "SI" and f2 == "SOL" and f3 == "RÉ":
    print("As frequências formam um acorde de SOL maior.")
elif f1 == "RÉ" and f2 == "SI" and f3 == "SOL":
    print("As frequências formam um acorde de SOL maior.")
else:
    print("As frequências NÃO formam um acorde de SOL maior.")
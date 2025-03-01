n = int(input())

for i in range (0, n):
    print("1", end="")
print()


for i in range(2, n):
    c = False
    f = False
    for i in range (0, n):
        if c == False:
            print("1" , end="")
            c = True
        elif i <= n-2:
            print("0", end="")
        else:
            print("1")
            f = True

        

for i in range (0, n):
    print("1", end="")
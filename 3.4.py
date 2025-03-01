a = int(input())
b = int(input())

if a < b:
    a, b = b, a
    
while  a >= b:
    print(a *2 + b)
    b = b + 2
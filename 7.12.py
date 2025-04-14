def calcdist(v1, v2):
    dist = 0
    for i in range(len(v1)):
        dist += (v1[i] - v2[i])**2
    return dist**0.5

v1 = [float(x) for x in input().split()]
v2 = [float(x) for x in input().split()]

print(calcdist(v1,v2))
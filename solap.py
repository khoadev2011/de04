import random
input()
ar = list(map(int, input().split()))
l_ar = []
for x in range(-100, 100):
    l_ar.append(ar.count(x))
print(l_ar.index(max(l_ar)) - 100)
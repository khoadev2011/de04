v = input()

for x in range(1, len(v)):
    vl = v[0:x]
    vr = v[x:len(v)]
    nv = vr + vl
    if nv == nv[::-1]:
        print(x)
        break
    if x == len(v):
        print(0)

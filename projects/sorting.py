v = [1,2,3,4,6,9,11,7]
n = []
sm = v[0]
for x in range(len(v)):
    for y in v:
        if sm > y:
            sm = y
    n.append(sm)
    v.remove(v[v.index(sm)])
    if len(v) >0:
        sm = v[0]
print(n)
v = [1,2,3,4,6,12,11,7]

for x in range(len(v)):
    swapped = False
    for j in range(0, len(v)-x-1):
        if v[j] > v[j+1]:
            (v[j],v[j+1]) = (v[j+1],v[j])
            swapped = True
    if swapped == False:
        break
print(v)
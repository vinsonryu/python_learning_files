#test_list[:0] = [6] /pop
v = [1,2,3,4,6,12,11,7]
lt = len(v)
for x in  range(1,lt):
    key = v[x]
    j = x-1
    while j >= 0 and key< v[j]:
        v[j + 1] = v[j]
        j -=1
    v[j +1] = key

print(v)
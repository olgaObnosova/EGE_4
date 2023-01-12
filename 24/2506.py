with open('2506') as f:
    f = f.readline()
k = maxx = 0
for x in f:
    if x == 'C':
        k += 1
        maxx = max(k, maxx)
    else:
        k = 0
print(maxx)

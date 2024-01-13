with open('5672.txt') as f:
    sp = []
    maxx = 0
    for line in f:
        sp.append(int(line))
        if int(line) % 73 == 0:
            maxx = max(maxx, int(line))
maxs = 0
k = 0
for i in range(len(sp)-1):
    if sp[i] >= maxx and sp[i + 1] >= maxx:
        k += 1
        maxs = max(maxs, sp[i] + sp[i + 1])

print(k)
print((maxs))

with open('27B_7827.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
maxc = maxn = maxs = 0
for i in range(k, len(sp)):
    if sp[i - k] % 2 == 0:
        maxc = max(maxc, sp[i - k])
    else:
        maxn = max(maxn, sp[i - k])
    if sp[i] % 2 == 0:
        maxs = max(maxs, sp[i] + maxn)
    else:
        maxs = max(maxs, sp[i] + maxc)
print(maxs)

with open('17.txt') as f:
    sp = []
    for x in f:
        sp.append(int(x))
k = 0
sp1=sp.copy()
sp1.sort()
maxxl=sp1[-3]
maxx = 0
for i in range(len(sp) - 2):
    l = 0
    if sp[i] % 2 == 0:
        l += 1
    if sp[i + 1] % 2 == 0:
        l += 1
    if sp[i + 2] % 2 == 0:
        l += 1
    if l <= 2 and (sp[i] + sp[i + 1] + sp[i + 2]) <= maxxl:
        k += 1
        maxx = max(maxx, sp[i] + sp[i + 1] + sp[i + 2])
print(k, maxx)
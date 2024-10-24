
with open('17-3.txt') as f:
    sp = []
    maxx = 0
    for x in f:
        sp.append(int(x))
        s=hex(int(x))[2:]
        #print(s)
        if len(s)>1 and s[-2:]=='0f':
            maxx = max(maxx, int(x))
k = 0
print(maxx)
maxs = 0
for i in range(len(sp) - 2):
    l = 0
    if sp[i] % 7 == 0:
        l += 1
    if sp[i + 1] % 7 == 0:
        l += 1
    if l == 1 and (sp[i] + sp[i + 1]) % maxx == 0:
        k += 1
        maxs = max(maxs, sp[i] + sp[i + 1])
print(maxx)
print(k, maxs)
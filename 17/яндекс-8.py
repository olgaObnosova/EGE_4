with open('17.txt') as f:
    sp = []
    maxx = 0
    for x in f:
        sp.append(int(x))
        if int(x) > 0 and len(str(int(x))) == 5 \
                and int(x) % 100 == 17:
            maxx = max(maxx, int(x))

k = 0
minn = float('inf')
for i in range(len(sp) - 2):
    l = 0
    if abs(sp[i]) % 100 == 17:
        l += 1
    if abs(sp[i + 1]) % 100 == 17:
        l += 1
    if abs(sp[i + 2]) % 100 == 17:
        l += 1
    if l >= 1 and abs(sp[i]) + abs(sp[i + 1]) + abs(sp[i + 2]) <= maxx:
        k += 1
        minn = min(minn, sp[i] + sp[i + 1] + sp[i + 2])
print(k, minn)
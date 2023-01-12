with open('17_15_12_22.txt') as f:
    minn = 10_000
    sp = []
    for line in f:
        sp.append(int(line))
        if abs(int(line)) % 10 == 5:
            minn = min(minn, int(line))

#print(sp)
#print(minn)
k = 0
maxx = -999999999999999
for i in range(len(sp) - 1):
    if abs(min(sp[i], sp[i + 1])) % 10 == 5 \
            and sp[i] ** 2 + sp[i + 1] ** 2 < minn ** 2:
        k += 1
        maxx = max(sp[i] ** 2 + sp[i + 1] ** 2, maxx)
print(k, maxx)
#print(minn)
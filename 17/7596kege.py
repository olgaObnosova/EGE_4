with open('17_7596.txt') as f:
    sp = []
    minn5 = float('inf')
    for x in f:
        if int(x) % 10 == 5 and 99 < int(x) < 1000:
            minn5 = min(minn5, int(x))
        sp.append(int(x))
k = 0
m = 999999999
print(minn5)
for i in range(len(sp) - 1):
    if ((len(str(sp[i])) == 3 and len(str(sp[i + 1])) != 3) or \
        (len(str(sp[i + 1])) == 3 and len(str(sp[i])) != 3)) \
            and (sp[i] + sp[i + 1]) % minn5 == 0:
        k += 1
        m = min(m, sp[i] + sp[i + 1])
print(k, m)
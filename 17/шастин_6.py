with open('17.txt') as f:
    sp = []
    maxx = 0
    for x in f:
        sp.append(int(x))
        if int(x) % 401 == 0:
            maxx = max(maxx, int(x))
print(maxx)
k = 0
minn = float('inf')
for i in range(len(sp) - 2):
    if sum(map(int, str(sp[i]))) != sum(map(int, str(sp[i + 1]))) \
            != sum(map(int, str(sp[i + 2]))) \
            and (sp[i] + sp[i + 1] + sp[i + 2]) > maxx:
        k += 1
        minn = min(minn, sp[i] + sp[i + 1] + sp[i + 2])
print(k, minn)
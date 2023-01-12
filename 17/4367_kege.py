with open('4367.txt') as f:
    minn = float('inf')
    sp = []
    for line in f:
        sp.append(int(line))
        if int(line) % 8 == 0 and int(line) != 8:
            minn = min(minn, int(line))
minn2 = float('inf')
k = 0
for i in range(len(sp) - 1):
    if sp[i] % minn == 0 and sp[i + 1] % minn == 0:
        k += 1
        if sp[i] + sp[i + 1] < minn2:
            minn2 = sp[i] + sp[i + 1]
            a = (sp[i], sp[i + 1])
print(k, max(a))

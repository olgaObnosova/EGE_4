with open('17.txt') as f:
    sp = []
    minn = float('inf')
    for x in f:
        sp.append(int(x))
        if abs(int(x)) % 100 == 25:
            minn = min(minn, int(x))
print(minn) #-75
k = 0
maxx = 0
for i in range(len(sp) - 2):
    l = 0
    if len(str(abs(sp[i]))) == 4:
        l += 1
    if len(str(abs(sp[i + 1]))) == 4:
        l += 1
    if len(str(abs(sp[i + 2]))) == 4:
        l += 1
    if l >= 2 and (sp[i] * sp[i + 1] * sp[i + 2]) <= minn ** 2:
        k += 1
        maxx = max(maxx, sp[i] * sp[i + 1] * sp[i + 2])
print(k, maxx)
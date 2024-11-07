with open('17_6089.txt') as f:
    sp = []
    maxx = 0
    for x in f:
        sp.append(int(x))
        if str(abs(int(x)))[-1] == '2': # abs(int(x))%10
            maxx = max(maxx, int(x))
print(maxx)
k = 0
maxs = 0
for i in range(len(sp)):
    if abs(sp[i]) % 3 == 0 and abs(sp[i]) % 7 != 0 \
            and abs(sp[i]) % 17 != 0 and \
            maxx % sp[i] == 0:
        k += 1
        maxs = max(maxs, sp[i])
print(k, maxs)
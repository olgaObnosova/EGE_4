with open('17_2388.txt') as f:
    sp = [int(x) for x in f]
k = 0
minn = 99999999
for i in range(len(sp) - 1):
    if (sp[i] % 5 == 0 and sp[i + 1] % 5 == 0 and \
            sp[i] % 3 != 0 and sp[i + 1] % 3 != 0):
        k += 1
        s = sp[i]+sp[i+1]
        if s > 0:
            minn=min(minn, s)
print(k, minn)

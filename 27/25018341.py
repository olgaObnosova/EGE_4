with open('25018341_b.txt') as f:
    n = int(f.readline())
    sp = []
    for line in f:
        sp.append(int(line))
maxx = 0
for i in range(len(sp)):
    s = 0
    for j in range(len(sp)):
        s += sp[j] * abs(j - i)
    maxx = max(maxx, s)
print(s)

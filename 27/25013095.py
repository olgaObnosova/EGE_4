s = 0
with open('25013095.txt') as f:
    n = f.readline()
    left = 0
    sp = []
    k = -1
    spsk = [0] * 16
    spost = [float('inf')] * 16
    for line in f:
        k += 1
        line = int(line)
        if line % 2 == 0:
            s += line
            if s< spost[line%16]:
                spost[line%16]=s
                spsk[line%16]=k
        sp.append((s, k))
print(sp)
print(spost)
print(spsk)
print(s%16)
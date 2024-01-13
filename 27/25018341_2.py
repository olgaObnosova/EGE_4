with open('25018341.txt') as f:
    n = int(f.readline())
    sp = []
    k = s = 0
    for line in f:
        s += int(line) * k
        k += 1
        sp.append(int(line))
summ = sum(sp)
maxx = 0
suml = sp[0]
sump = 0
for i in range(1, len(sp)):
    a = s + sump - suml
    sump = summ - suml
    suml += sp[i]
    if a > maxx:
        maxx = a
print(maxx)

with open('27_A_5142.txt') as f:
    n, m = map(int, f.readline().split())
    sv = [0] * 989 #99 млн
    sp = [0] * 989
    for x in f:
        a, b = map(int, x.split())
        sv[a] = b
        b = b//50 + bool(b%50)
        sp[a]=b
maxv = 0
minp = float('inf')
for i in range(m,989-m):
    if sv[i]!=0:
        sumv = sum(sv[i-m : i + m + 1])
        sump = sum(sp[i - m: i + m + 1])
        #print(sump)
        if sumv>=maxv:
            maxv = sumv
            minp = sump
            otv = i
print(maxv)
print(otv)
print(minp)


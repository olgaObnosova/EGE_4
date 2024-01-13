with open('25019141.txt') as f:
    n, m = map(int, f.readline().split())
    sp = [int(x) for x in f]
sp.sort(reverse=True)
otv = []
while len(sp) > 0:
    i = 0
    s = 0
    while s < m:
        if s + sp[i] <= m:
            s += sp[i]
            sp.remove(sp[i])
        else:
            i += 1
        if i == len(sp):
            break
        print(sp, s)
        # print(s)
    otv.append(s)
print((otv), sp, s)

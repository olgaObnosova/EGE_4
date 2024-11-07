with open('26-15.txt') as f:
    n=int(f.readline())
    sp=[]
    k=0
    for x in f:
        k+=1
        a, b = map(int, x.split())
        sp.append((a, k, 'shl'))
        sp.append((b, k, 'okr'))
sp.sort()
m = 0
pr, lev = n, 1
lenta=[0]*(n+1)
count = 0
tr = ''
for x in sp:
    vr, idd, tp = x
    if idd not in lenta:
        if tp=='shl':
            lenta[lev]=idd
            m = lev
            tr = 'shl'
            lev+=1
            count+=1
        if tp=='okr':
            lenta[pr]=idd
            m = pr
            tr = 'okr'
            pr-=1
print(lenta[m], count - 1, tr)
#print(lenta)



with open('pr') as f:
    n, m=map(int,f.readline().split())
    sp=[0]*m
    summ=0
    k=nac=0
    for line in f:
        a, b = map(int, line.split())
        sp[a]=b
        summ+=b
        nac+=k*b
        k+=1
lev=sp[0]
minn=float('inf')
for i in range(1, len(sp)):
    pr=summ-lev
    nac=nac+lev-pr
    lev+=sp[i]
    if nac<=minn and sp[i]==0:
        minn=nac
        otv=i
print(otv)



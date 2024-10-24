with open('17-3.txt') as f:
    maxx=0
    sp=[]
    minn=float('inf')
    for x in f:
        x=int(x)
        sp.append(x)
        maxx=max(maxx, x)
        minn=min(minn, x)
sr=(maxx+minn)/2
dl=len(sp)
k=maxs=0
for i in range(dl//2):
    if (sp[i]< sr and sp[dl-1-i]>sr) or\
        (sp[i] > sr and sp[dl - 1 - i] < sr):
        k+=1
        maxs=max(maxs, sp[i]+sp[dl-1-i])
print(k, maxs)



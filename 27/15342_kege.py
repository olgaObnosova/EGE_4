with open('pr') as f:
    n, k = map(int, f.readline().split())
    sp=[]
    st=benz=0
    prb=[]
    levb=[]
    for x in f:
        a, b = map(int, x.split())
        b = b//3 + bool(b % 3)
        sp.append([a,b])
        benz+=b
        if a==k:
            levb=levb+[b]

        elif a<k//2:
            prb.append(b)
        else:
            levb.append(b)
for i in range(1,len(sp)):
    st+=min(abs(sp[0][0]-sp[i][0]),abs(k-sp[i][0]+sp[0][0]))*sp[i][1]
print(sp)
print(prb, levb, st)
minn=float('inf')
for i in range(1, n):
    r=abs(sp[i][0]-sp[i-1][0])
    st = st - sum(prb) * r + sum(levb) * r
    s=prb.pop(0)
    levb = levb+[s]
    #st=st-sum(prb)*r+sum(levb)*r
    s=levb.pop(0)
    prb = prb+[s]
    print(prb,levb,st)
    minn=min(st, minn)
print(minn)




with open('26-16.txt') as f:
    n=int(f.readline())
    k=int(f.readline())
    sp=[]
    for x in f:
        vr, nom, zv = map(int, x.split())
        sp.append([zv, vr, nom-1])
sp.sort()
stv=[0]*(k)
stn=[0]*k
c=0
pred=posl=0
for x in sp:
    zv, vr, nom = x
    if vr <= 1320:
        if vr > stv[nom]:
            stv[nom] = vr+120
            pred=posl
            posl=nom
            c+=1
        else:
            for i in range(k):
                if vr>stv[i]:
                    stv[i]=vr+120
                    pred = posl
                    posl = i
                    c+=1
                    break
    #print(x, c, stv)
print(c)
print(pred+1)



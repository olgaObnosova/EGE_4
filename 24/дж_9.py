with open('24_дж9.txt') as f:
    maxlen=0
    sim=''
    sp=[]
    l=0
    for x in f:
        l+=1
        k = 1
        maxlen=0
        sim=''
        for i in range(len(x)-1):
            if x[i]==x[i+1]:
                k+=1
                if k>maxlen:
                    maxlen=k
                    sim=x[i]
                    sp.append([maxlen,sim, l])
            else:
                k=1
sp.sort()
#print(sp)
ka=kb=kc=kd=ke=kf=0
for x in sp:
    if x[1]=='A':
        ka+=1
    if x[1]=='B':
        kb+=1
    if x[1]=='C':
        kc+=1
    if x[1]=='D':
        kd+=1
    if x[1]=='E':
        ke+=1
    if x[1]=='F':
        kf+=1
print(ka, kb, kc, kd, ke, kf)



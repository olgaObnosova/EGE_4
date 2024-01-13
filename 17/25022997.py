with open('17.txt') as f:
    sp=[]
    minn=float('inf')
    for line in f:
        sp.append(int(line))
        if abs(int(line))<minn:
            minn=abs(int(line))
k=0
maxx=0
for i in range(len(sp)-1):
    if sp[i]*sp[i+1]<0 and sp[i]+sp[i+1]>0 and \
            (sp[i]+sp[i+1])%minn==0:
        k+=1
        maxx=max(maxx,sp[i]+sp[i+1])
print(k, maxx)
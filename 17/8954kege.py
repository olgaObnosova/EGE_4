with open('17_8954.txt') as f:
    sp=[]
    maxx=0
    for line in f:
        sp.append(int(line))
        if hex(int(line))[-2:]=='0f':
            maxx=max(maxx,int(line))
#print(maxx, hex(maxx))
k=maxs=0
for i in range(len(sp)-1):
    if ((sp[i]%7==0 and sp[i+1]%7!=0) \
            or (sp[i+1]%7==0 and sp[i]%7!=0)) and \
            (sp[i]+sp[i+1])%maxx==0:
        k+=1
        maxs=max(maxs,sp[i]+sp[i+1])
print(k, maxs)
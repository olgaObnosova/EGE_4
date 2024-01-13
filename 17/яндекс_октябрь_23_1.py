with open('17_yand.txt') as f:
    sp=[]
    maxx=0
    for x in f:
        sp.append(int(x))
        if 99<int(x)<1000:
            maxx=max(maxx, int(x))
k=0
maxs=0
print(maxx)
for i in range(len(sp)-1):
    if ((len(str(abs(sp[i])))!=3 and len(str(abs(sp[i+1])))==3) or \
        (len(str(abs(sp[i])))==3 and len(str(abs(sp[i+1])))!=3)) and \
           (sp[i]+sp[i+1])>=maxx:
            k+=1
            maxs=max(maxs, sp[i]+sp[i+1])
print(k, maxs)
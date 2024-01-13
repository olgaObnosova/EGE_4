with open('17_6752.txt') as f:
    sp = []
    k3=0
    maxx=0
    for x in f:
        sp.append(int(x))
        if abs(int(x))%3==0:
            k3+=1
k=0
maxs=0
for i in range(len(sp)-1):
    if (sp[i]<0 or sp[i+1]<0) and (sp[i]+sp[i+1])<k3:
            maxs=max(maxs, sp[i]+sp[i+1])
            k+=1
print(k, maxs)
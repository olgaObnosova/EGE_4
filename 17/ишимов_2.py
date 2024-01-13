with open('17.txt') as f:
    sp=[]
    maxx=0
    for x in f:
        sp.append(int(x))
        if abs(int(x))%10==3:
            maxx=max(maxx, int(x))
k=maxs=0
for i in range(len(sp)-2):
    if (abs(sp[i])%2+abs(sp[i+1])%2+abs(sp[i+2])%2==1) and \
        (sp[i]+sp[i+1]+sp[i+2])>=maxx:
        k+=1
        maxs=max(maxs, sp[i]+sp[i+1]++sp[i+2])
print(maxx)
print(k, maxs)

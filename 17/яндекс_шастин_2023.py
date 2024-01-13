with open('17.txt') as f:
    sp=[]
    maxx=maxs=0
    k=0
    for x in f:
        sp.append(int(x))
        if int(x)%100==18:
            maxx=max(maxx, int(x))
print(maxx)
for i in range(len(sp)-2):
    if not('3' in str(sp[i]) and '3' in str(sp[i+1])\
            and '3' in str(sp[i+2])) and \
       ((sp[i]+sp[i+1]+sp[i+2])<=maxx):
        k+=1
        maxs=max(maxs, sp[i]+sp[i+1]+sp[i+2])
print(k, maxs)
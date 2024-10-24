with open('17-dg7.txt') as f:
    smp=kp=0
    sp=[]
    for x in f:
        x=int(x)
        sp.append(x)
        if x>0:
            smp+=x
            kp+=1
srp=smp/kp
print(srp)
k=maxs=0
for i in range(len(sp)-1):
    summ=0
    if sp[i]>srp or sp[i+1]>srp:
        #print(sp[i],sp[i+1])
        k+=1
        s1=str(abs(sp[i]))
        s2 = str(abs(sp[i+1]))
        for x in s1:
            summ+=int(x)
        maxs = max(maxs, summ)
        summ=0
        for x in s2:
            summ+=int(x)
        maxs=max(maxs,summ)
print(k, maxs)
with open ('2024_var3_ege26_16457.txt') as f:
    n = int(f.readline())
    sp=[]
    for x in f:
        pr,obs, okn = map(int, x.split())
        sp.append([pr, obs, okn])
sp.sort()
#print(sp[:10])
sp1=[]
sp2=[]
sp3=[]
k=0
for x in sp:
    pr, obs, okn = x
    if okn==1:
        if len(sp1)==0:
            sp1.append(pr+obs)
        elif len(sp1) <=8:
            if sp1[0]<=pr and len(sp1)<=8:
                sp1.pop(0)
                sp1.append(sp1[-1]+obs)
                k+=1
            elif len(sp1) < 8:
                sp1.append(sp1[-1] +obs)
                k+=1
    elif okn==2:
        if len(sp2)==0:
            sp2.append(pr + obs)
        elif len(sp2) <= 8:
            if sp2[0] <= pr and len(sp2)<=8:
                sp2.pop(0)
                sp2.append(sp2[-1]+obs)
                k+=1
            elif len(sp2) < 8:
                sp2.append(sp2[-1]+obs)
                k+=1
    elif okn==3:
        if len(sp3)==0:
            sp3.append(pr + obs)
        elif len(sp3) <= 8:
            if sp3[0] <= pr and len(sp3)<=8:
                sp3.pop(0)
                sp3.append(sp3[-1]+obs)
                k+=1
            elif len(sp3)<8:
                sp3.append(sp3[-1]+obs)
                k+=1
    else:
        t1 = len(sp1)
        t2 = len(sp2)
        t3 = len(sp3)
        minn = min(t1, t2, t3)
        if minn == t1:
            if len(sp1)==0:
                sp1.append(pr+obs)
            elif len(sp1) <= 8:
                if sp1[0] <= pr and len(sp1)<=8:
                    sp1.pop(0)
                    sp1.append(sp1[-1] + obs)
                    k+=1
                elif len(sp1) < 8:
                    sp1.append(sp1[-1] + obs)
                    k+=1
        elif minn==t2:
            if len(sp2)==0:
                sp2.append(pr+obs)
            elif len(sp2) <= 8:
                if sp2[0] <= pr and len(sp2)<=8:
                    sp2.pop(0)
                    sp2.append(sp2[-1] + obs)
                    k+=1
                elif len(sp2)<8:
                    sp2.append(sp2[-1] + obs)
                    k+=1
        elif minn==t3:
            if len(sp3)==0:
                sp3.append(pr+obs)
            elif len(sp3) <= 8:
                if sp3[0] <= pr and len(sp3)<=8:
                    sp3.pop(0)
                    sp3.append(sp3[-1] + obs)
                    k+=1
                elif len(sp3)<8:
                    sp3.append(sp3[-1] + obs)
                    k+=1
    #print(sp1, sp2, sp3)
print(k)







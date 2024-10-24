import fnmatch as f
for i in range(126150, 10**10, 21025):
    if f.fnmatch(str(i),'12*34?5'):
        i=str(i)
        kc=kn=0
        for x in i:
            if int(x)%2==0:
                kc+=1
            else:
                kn+=1
        if kc==kn:
            print(int(i), int(i)//21025)

import fnmatch as f
for i in range(157424, 10**8):
    if f.fnmatch(str(i),'*15*7424'):
        k=0
        if i%111==0:
            k+=1
        if i%113==0:
            k+=1
        if i%127==0:
            k+=1
        if k==1:
            print(i, i/111, i/113,i/127)


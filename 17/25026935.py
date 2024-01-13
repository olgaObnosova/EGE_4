with open('17.txt') as f:
    sp=[]
    minn=float('inf')
    for line in f:
        if 99<int(line)<1000 and line[0]!=line[1]\
            and line[1]!=line[2] and line[0]!=line[2]:
            minn=min(minn, int(line))
        sp.append(int(line))
k=0
mins=float('inf')
for i in range(len(sp)):
    if (sp[i]*sp[len(sp)-i-1])%minn==0:
        k+=1
        mins=min(mins,sp[i]+sp[len(sp)-i-1] )
print(k, mins)
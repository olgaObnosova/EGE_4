with open('pr') as f:
    n, m=map(int,f.readline().split())
    sp=[0]*m
    for line in f:
        a, b = map(int, line.split())
        sp[a]=b
#print(sp)
minn=float('inf')
sp2=[]
for i in range(len(sp)):
    s=0
    if sp[i]==0:
        for j in range(len(sp)):
            s+=abs(i-j)*sp[j]
        sp2.append((s,i))
        if s<=minn:
            minn=s
            otv=i
print(otv)
print(min(sp2))
#print(sp2)
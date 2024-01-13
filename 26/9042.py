with open('26.txt') as f:
    k,n=map(int,f.readline().split())
    sp1=[]
    sp=[]
    for line in range(k):
        sp1.append([0,int(f.readline())])
#print(sp1,len(sp1))
    for line in f:
        a,b,c=map(int,line.split())
        sp.append((a,b,c))
#print(sp,len(sp))
sp.sort()
s=r=0
for x in sp:
    st,e,v=x
    for i in range(len(sp1)):
        if st>sp1[i][0] and v<=sp1[i][1]:
            sp1[i][0]=e
            s+=v
            r=v
            break
print(s,r)
with open('27(B).txt') as f:
    n=f.readline()
    k=int(f.readline())
    sp=[]
    maxx=maxxs=0
    for line in f:
        sp.append(int(line))
#print(sp,len(sp))
b=0
for i in range(k,len(sp)):
    if maxx<sp[i-k]:
        maxx=sp[i-k]
        a=i-k
    if maxxs<=maxx+sp[i]:
        maxxs=maxx+sp[i]
        b=max(b,abs(a-i))
print(maxxs,a,b,k)
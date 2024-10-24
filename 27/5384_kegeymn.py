with open('27_A_5384.txt') as f:
    n,k=map(int, f.readline().split())
    sp = []
    for x in f:
        a, b=map(int,x.split())
        b=b//k+bool(b%k)
        sp.append([a, b])
minn=float('inf')
st=0
sum=0
for i in range(n):
    st+=abs(sp[0][0]-sp[i][0])*sp[i][1]
    sum+=sp[i][1]
r=0
left=sp[0][1]
for i in range(1, n):
    pravs=sum-left
    r=abs(sp[i][0]-sp[i-1][0])
    st=st+r*left-r*pravs
    left+=sp[i][1]
    if st<minn:
        minn=st
print(minn)
print(sp[:10])
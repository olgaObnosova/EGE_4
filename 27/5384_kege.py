with open('27_A_5384.txt') as f:
    n,k=map(int, f.readline().split())
    spsum = []
    for x in f:
        a, b=map(int,x.split())
        b=b//k+bool(b%k)
        spsum.append([a, b])
minn=float('inf')
for i in range(len(spsum)):
    s=0
    for j in range(0, len(spsum)):
        s+=abs(spsum[i][0]-spsum[j][0])*spsum[j][1]
    print(s)
    if s<minn:
        minn=s
print(minn)
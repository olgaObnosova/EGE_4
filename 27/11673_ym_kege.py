with open('27B_11673.txt') as f:
    k=int(f.readline())
    n=int(f.readline())
    sp=[int(x) for x in f]
ind=cnt=0 #500000000
for i in range(n):
    while ind<n and abs(sp[i]-sp[ind])<=k:
        ind+=1
    cnt+=n-ind
print(cnt*2)
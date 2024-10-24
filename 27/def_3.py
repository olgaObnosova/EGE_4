with open('27_A_11.txt') as f:
    k=int(f.readline())
    n=int(f.readline())
    sp=[int(x) for x in f]
maxx=maxc=maxn=maxl=0 #185463
for i in range(2*k, n):
    maxl=max(maxl,sp[i-2*k])
    if (maxl+sp[i-k])%2==0:
        maxc=max(maxc, maxl+sp[i-k])
    else:
        maxn = max(maxn, maxl + sp[i - k])

    if sp[i]%2==0:
        maxx=max(maxx,maxn+sp[i])
    else:
        maxx = max(maxx, maxc + sp[i])
print(maxx, maxn, maxc, maxl)

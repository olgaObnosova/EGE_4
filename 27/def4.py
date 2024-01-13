with open('27_B.txt') as f:
    k=int(f.readline())
    n=int(f.readline())
    sp=[int(x) for x in f]
maxn26=maxc26=maxn=maxc=maxs=0
for i in range(k,n):
    if sp[i-k]%26==0:
        if sp[i-k]%2==0:
            maxc26=max(maxc26,sp[i-k])
        else:
            maxn26 = max(maxn26, sp[i - k])
    else:
        if sp[i-k]%2==0:
            maxc=max(maxc,sp[i-k])
        else:
            maxn = max(maxn, sp[i - k])
    if sp[i]%26==0:
        if sp[i]%2==0:
            maxs=max(maxs,sp[i]+maxn)
            maxs = max(maxs, sp[i] + maxn26)
        else:
            maxs = max(maxs, sp[i] + maxc)
            maxs = max(maxs, sp[i] + maxc26)
    else:
        if sp[i]%2==0:
            maxs = max(maxs, sp[i] + maxn26)
        else:
            maxs = max(maxs, sp[i] + maxc26)
print(maxs)
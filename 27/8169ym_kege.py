with open('27_B_8169.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
maxc = maxn = maxx = 0
for i in range(n-k):
    if sp[i]%26==0:
        maxc=max(maxc, sp[i])
    elif sp[i]%2!=0:
        maxn=max(maxn, sp[i])
    if sp[i+k]%26==0:
        maxx=max(maxx, maxn+sp[i+k])
    elif sp[i+k]%2!=0:
        maxx=max(maxx, sp[i+k]+maxc)
print(maxx)


with open('17-4.txt') as f:
    f=[int(x) for x in f]
minn=float('inf')
print(f)
for x in f:
    if x>0 and x%10==4:
        minn=min(minn, x)
k=0
maxs=0
for i in range(len(f) - 2):
    a, b, c = abs(f[i]), abs(f[i+1]), abs(f[i+2])
    sa = sum([int(x) for x in str(a)])
    sb = sum([int(x) for x in str(b)])
    sc = sum([int(x) for x in str(c)])
    if sa+sb+sc == minn:
        k+=1
        maxs = max(maxs, f[i] + f[i+1] + f[i+2])
print(k, maxs)

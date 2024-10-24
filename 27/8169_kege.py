with open('27_A_8169.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
maxx = 0
for i in range(n-k):
    for j in range(i+k, n):
        if abs(sp[i]-sp[j])%2!=0 \
                and (sp[i]%26==0 or sp[j]%26==0):
            maxx=max(maxx, sp[i]+sp[j])
print(maxx)
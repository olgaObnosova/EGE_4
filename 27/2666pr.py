with open('27.txt') as f:
    n=int(f.readline())
    sp=[int(x) for x in f]
maxx=0
for i in range(n-1):
    for j in range(i+1,n):
        if (sp[i]*sp[j]) %6==0:
            maxx=max(maxx, sp[i]*sp[j])
print(maxx)

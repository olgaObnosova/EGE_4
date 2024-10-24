with open('27A_11673.txt') as f:
    k=int(f.readline())
    n=int(f.readline())
    sp=[int(x) for x in f]
print(max(sp))
cnt=0
for i in range(n-1):
    for j in range(i+1, n):
        if abs(sp[i]-sp[j])>k:
            cnt+=1
print(cnt*2)
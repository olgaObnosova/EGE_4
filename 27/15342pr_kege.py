with open('pr') as f:
    n, k = map(int, f.readline().split())
    sp=[]
    st=0
    minn=float('inf')
    for x in f:
        a, b=map(int, x.split())
        b=b//3+bool(b%3)
        sp.append([a, b])
#print(sp)
for i in range(n):
    st = 0
    for j in range(n):
        if sp[i][0]<k//2:
            if abs(sp[i][0]-sp[j][0])<abs(k-sp[j][0]+sp[i][0]):
                st+=abs(sp[i][0]-sp[j][0])*sp[j][1]
            else:
                st+=abs(k-sp[j][0]+sp[i][0])*sp[j][1]
        else:
            if abs(sp[i][0]-sp[j][0])<abs(k-sp[i][0]+sp[j][0]):
                st+=abs(sp[i][0]-sp[j][0])*sp[j][1]
            else:
                st+=abs(k-sp[i][0]+sp[j][0])*sp[j][1]
    print(st, sp[i])
    minn=min(minn, st)
print(minn)
with open('27A_4713.txt') as f:
    n=int(f.readline())
    sp=[]
    for line in f:
        a = int(line.split()[0])
        b = int(line.split()[1])
        b = b//36 + bool(b%36)
        sp.append((a,b))
minn = float('inf')
for i in range(len(sp)):
    s = 0
    for j in range(len(sp)):
        s+=abs(sp[i][0]-sp[j][0])*sp[j][1]
    minn = min(minn,s)
print(minn)




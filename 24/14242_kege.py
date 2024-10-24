with open('pr') as f:
    f=f.readline()
sp=[[0]*4 for i in range(len(f))]#[гл, согл,чет,нечет]
gl='AE'
sogl='BD'
ch='02'
nch='13'
for i in range(len(f)):
    sp[i]=sp[i-1].copy()
    if f[i] in gl:
        sp[i][0]=sp[i-1][0]+1
    if f[i] in sogl:
        sp[i][1] = sp[i - 1][1] + 1
    if f[i] in ch:
        sp[i][2] = sp[i - 1][2] + 1
    if f[i] in nch:
        sp[i][3] = sp[i - 1][3] + 1
maxl=0
print(sp)
for i in range(len(f)):
    for j in range(i+1, len(f)):
        r1=sp[j][0]-sp[i][0]
        r2=sp[j][1]-sp[i][1]
        r3=sp[j][2]-sp[i][2]
        r4=sp[j][3]-sp[i][3]
        if r1==r2 and r3==r4:
            maxl=max(maxl, abs(j-i))
print(maxl)


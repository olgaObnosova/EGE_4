with open('2_27_A_EGKR.txt') as f:
    n=int(f.readline())
    sp=[int(x) for x in f]
spc=[sp[0]]
for i in range(1, n):
    spc.append(spc[-1]+sp[i])
#print(spc)
sp237=[float('inf')]*263
spind=[0]*263
s=0
maxs=maxx=0
for i in range(n):
    ost=spc[i]%263
    if spc[i] < sp237[ost]:
        sp237[ost]=spc[i]
        spind[ost]=i
    if abs(spc[i]-sp237[ost]) >=maxs:
        maxs=abs(spc[i]-sp237[ost])
        l = i - spind[ost]
        maxx = max(maxx, l)
print(maxx)


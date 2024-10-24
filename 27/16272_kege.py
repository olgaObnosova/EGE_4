
with open('pr') as f:
    k=int(f.readline())
    n=int(f.readline())
    sp=[int(x) for x in f]
s=sum(sp)
sps=[sp[0]] #6-1==11-6
for i in range(1, n):
    sps.append(sps[-1]+sp[i])
print(s)
print(sps)
for x in sps:
    print(s-x)
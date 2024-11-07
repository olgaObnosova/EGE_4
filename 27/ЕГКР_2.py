with open('27_B._EGKR.txt') as f:
    n=int(f.readline())
    sp = [int(x) for x in f]
sp137=[]
sps=[]
s=maxl=maxs=0
for i in range(n):
    if sp[i]%137==0:
        s+=sp[i]
    if sp[i]%137!=0:
        sp137.append([i, sp[i], sp[i]%137])
        sps.append([s, i])
        s = 0
sps.append(s)
print(len(sp137))
print(sps)
print(1325685-1000000)
print(n-1325685)





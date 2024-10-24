with open('pr') as f:
    n=int(f.readline())
    sp=[int(x) for x in f]
spr=[]
for i in range(1, n):
    spr.append(sp[i]-sp[i-1])
sps=[spr[0]]
for i in range(1,len(spr)):
    sps.append(sps[i-1]+spr[i])
print(spr)
print(sps)
maxx=0
minn=float('inf')
per=otv=0
for i in range(len(sps)):
    if sps[i]<=minn:
        minn = min(minn, sps[i])
        per = i
    if sps[i] - minn >= maxx:
        maxx = sps[i] - minn
        #print(i, per, maxx, minn, sps[i])
        permaxx=i
print(otv)
print(maxx)
print(abs(per - permaxx)+1)





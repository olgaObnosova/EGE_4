with open('27A_7603.txt') as f:
    n=int(f.readline())
    k = int(f.readline())
    sp=[int(x) for x in f]
maxs=maxx=0
for i in range(k, len(sp)):
    maxx=max(maxx,sp[i-k])
    maxs=max(maxs, maxx+sp[i])
print(maxs)




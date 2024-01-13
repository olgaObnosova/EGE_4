with open('27_B_8962.txt') as f:
    k=int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
maxx=maxs=0
maxx2=max(sp[:k])
for i in range(k,len(sp)):
    maxx=max(sp[i-k], maxx)
    if sp[i]>maxx2:
        maxx2=sp[i]
        maxs=max(maxs,sp[i]+maxx)
print(maxs)
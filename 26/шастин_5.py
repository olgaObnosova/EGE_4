with open('26-12.txt') as f:
    n, s, v = map(int, f.readline().split())
    sp=[int(x) for x in f]
sp.sort()
print(n, v)
i=k=0
zapr=[]
v1=v
while i<n-1 and sp[i]<=v1:
    if sp[i+1]>v1:
        k+=1
        zapr.append((sp[i],i))
        v1 = v + sp[i]
    i+=1
print(zapr)
print(sp[i],sp[i-1], i, v,s, k)

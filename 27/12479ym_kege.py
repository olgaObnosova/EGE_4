with open('27-A_12479.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
maxx1 = maxx = 0
for i in range(k,n):
    if sp[i-k]>maxx1:
        maxx1=sp[i-k]
        ind=i-k
    if maxx1+sp[i]+abs(ind-i)>maxx:
        maxx=maxx1+sp[i]+abs(ind-i)
print(maxx)

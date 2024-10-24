with open('26_12187.txt') as f:
    k=int(f.readline())
    n=int(f.readline())
    t=f.readline()
    vm=[int(x) for x in t.split()]
    sp=[]
    for x in f:
        a,b,c=map(int, x.split())
        sp.append([b,a,c])
sp.sort()
#print(sp)
d=[-1]*k
cnt=0
otv=0
for x in sp:
    t, v, e = x
    for i in range(k):
        if t < 1440 and t>=d[i]+1 and v<=vm[i]:
            d[i]=e
            otv=i
            cnt+=1
            #print(d,cnt, x)
            break
print(cnt, otv+1)
print(d[otv])

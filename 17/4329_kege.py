def fr(n):
    s=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s

maxd=ch=0
sp=[]
with open('17_4329.txt') as f:
    for x in f:
        x=int(x)
        sp.append(x)
        r = fr(x)
        if len(r)>maxd:
            maxd=len(r)
            ch=x
            delit=r
cnt=maxx=0
for i in range(len(sp)-1):
    p1 = fr(sp[i])
    p2 = fr(sp[i+1])#p1&p2
    if len(p1&delit)>=3 and len(p2&delit)>=3:
        cnt+=1
        g=len(p1&p2)
        maxx=max(maxx,g)
print(cnt, maxx)






from collections import Counter
def delit(n):
    d=2
    c= Counter()
    while n%2==0:
        c.update([d])
        n//=2
    d=3
    while d*d<=n:
        if n%d==0:
            c.update([d])
            n=n//d
        else:
            d+=2
    if n!=1:
        c.update([n])
    return c
st=0
with open('25013098A.txt') as f:
    n,m =map(int,f.readline().split())
    f = [int(f.readline()) for _ in range(n)]
d=delit(f[0])
#print(d)
minlen=float('inf')       
for i in range(1,len(f)):
    last = Counter()
    while len(d)>=m:
        minlen= min(minlen, i-st)
        last= delit(f[st])
        #print(last, f[st], st, i)
        d=d-last
        st+=1
    if len(last)>0:
        st-=1
        d = d + last
    d = d + delit(f[i])
print(minlen)
    
            

    

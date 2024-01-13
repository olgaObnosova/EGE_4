import fnmatch as f
def delit(n):
    s=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return sum(s)
k=0
for i in range(500_001,1000000):
    sm=delit(i)
    if f.fnmatch(str(sm),'*7?'):
        print(i, sm)
        k+=1
        if k==5:
            break
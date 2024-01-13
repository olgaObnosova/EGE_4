import fnmatch as f

def fn(n):
    s=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s
for i in range(10**5,-1,-1):
    d=fn(i)
    dm=[]
    k=0
    for x in d:
        if f.fnmatch(str(x),'1?2*'):
            dm.append(x)
            k+=1
    dm.sort()
    if k>=5:
        print(i, dm[4])


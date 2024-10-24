import fnmatch as f
def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
sp=[]
for i in range(2, 10_000):
    if pr(i):
        sp.append(i)
def d(n):
    global sp
    k=list()
    while n!=1:
        for x in sp:
            while n%x==0:
                n=n//x
                k.append(x)
            if n==1:
                break
    return k

for i in range(202, 10**4):
    #print(i)
    if f.fnmatch(str(i), '*2?2'):
        t=d(i)
        if len(t)==7:
            print(i, max(t))



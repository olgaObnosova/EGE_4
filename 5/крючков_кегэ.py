def tr(n):
    s=''
    while n!=0:
        s+=str(n%3)
        n=n//3
    return s[::-1]
minn=float('inf')
for i in range(1, 100000):
    n=tr(i)
    n=n.replace('0','*')
    n=n.replace('1','@')
    n=n.replace('2','0')
    n=n.replace('@','2')
    n=n.replace('*','1')
    n=int(n,3)
    n=tr(n)
    n=n[::-1]
    sm=tr(sum(map(int, str(n))))
    n=n+str(sm)
    if len(n)>0:
        r=int(n, 3)
        if r>10**4:
            minn=min(minn, r)
print(minn)
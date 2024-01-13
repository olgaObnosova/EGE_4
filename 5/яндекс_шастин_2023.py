def pyt(n):
    s=''
    while n>0:
        s+=str(n%5)
        n//=5
    return s[::-1]
minn=99999999999
for i in range(10, 1000):
    n=pyt(i)
    if i%5==0:
        n=n+n[-3:]
    else:
        ost=pyt(i%5*5)
        n=ost + n
    r=int(n, 5)
    if r>375:
        print(i)
        break
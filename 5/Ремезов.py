def sh(n):
    s=''
    while n>0:
        s+=str(n%6)
        n=n//6
    return s[::-1]
maxx=0
for i in range(11,1000):
    n=sh(i)
    k5=n.count('5')
    k4=n.count('4')
    if k5==k4:
        n=sh(k5)+n
    else:
        n=n+sh(n.count('0'))
    r=int(n, 6)
    if r>255:
        maxx=max(maxx, r)
print(maxx)
def perev(n):
    s=''
    while n!=0:
        s+=str(n%7)
        n=n//7
    return s[::-1]
for x in range(2030):
    a=7**170+7**100-x
    ch=perev(a)
    if ch.count('0')==71:
        print(x)

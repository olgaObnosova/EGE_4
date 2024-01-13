def pyt(n):
    s=''
    while n>0:
        s+=str(n%5)
        n//=5
    return s[::-1]
for i in range(1000, 10000):
    n=pyt(i)
    n1=n[::-1]
    r = abs(int(n,5)-int(n1,5))
    if r==100:
        print(i)


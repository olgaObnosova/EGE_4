def pal(n):
    if len(n)%2==0:
        if len(set(n))==1 or len(set(n))%2==0:
            return True
def p(n):
    s=''
    while n>0:
        s+=str(n%5)
        n=n//5
    return s[::-1]
sp=[]
print(pal('125512'))
for i in range(1,7**7):
    if i%16==15:
        sp.append(p(i))



def f(n, k):
    s=''
    while n!=0:
        s+=str(n%k)
        n=n//k
    return s[::-1]
s=0
for i in range(1, 96):
    a1=f(i, 3)
    a2=f(i, 5)
    if a1[-2:]=='21' and a2[0]=='3':
        s+=i
print(s)
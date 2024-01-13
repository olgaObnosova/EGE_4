mx=0
for i in range(100):
    n=bin(i)[2:]
    if i%3==0:
        n=n+n[-3:]
    else:
        ost=bin(i%3*3)[2:]
        n=n+ost
    r=int(n,2)
    if r<=170:
        mx=max(mx,r)
print(mx)
minn=float('inf')
for i in range(1, 1000):
    n=bin(i)[2:]
    if i%3==0:
        n=n+n[-3:]
    else:
        ost=(i%3)*3
        ost=bin(ost)[2:]
        n=n+ost
    r=int(n, 2)
    if r>151:
        minn=min(minn, r)
print(minn)


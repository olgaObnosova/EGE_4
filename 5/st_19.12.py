s = set()
otr = range(200, 250)
k = 0
for n in range(1, 100):
    r=bin(n)[2:]
    ost=bin(n%4)[2:]
    r=r+ost
    r=int(r, 2)
    if r in otr:
        k+=1
    print(n, r)
print(k)

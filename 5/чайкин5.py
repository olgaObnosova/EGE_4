maxx=0
minn=float('inf')
for i in range(2, 10000):
    n=bin(i)[2:]
    k0=k1=0
    for j in range(1, len(n), 2):
        if n[j]=='0':
            k0+=1
        else:
            k1+=1
    if k0 > k1:
        n = n.replace('1','2')
        n = n.replace('0', '1')
        n = n.replace('2', '0')
    else:
        n1=n[0]
        for j in range(1, len(n)):
            if j%2!=0:
                n1+='1'
            else:
                n1+=n[j]
        n=n1
    r = int(n,2)
    if r<=1337:
        if r>maxx:
            maxx=r
            print(r, i)

print(maxx)




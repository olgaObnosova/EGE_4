minn=99999999999
for n in range(1, 1000):
    r=bin(n)[2:]
    k=r.count('1')
    if  k%2==0:
        r='11'+r
    else:
        r=r+'00'
    r=int(r, 2)
    if r>116:
        print(n)
        break


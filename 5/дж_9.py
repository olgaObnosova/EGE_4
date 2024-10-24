minn=999999999
for n in range(1, 100):
    n1=n
    n=str(n)+str(n)[-1]
    n=int(n)
    r=bin(n)[2:]
    k=r.count('1')
    if k%2!=0:
        r=r+'1'
    else:
        r=r+'0'
    r=int(r, 2)
    if r>413:
        print(n1, r)
        break
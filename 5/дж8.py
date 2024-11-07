for n in range(1, 1000):
    r=bin(n)[2:]
    k=r.count('1')
    if k%2!=0:
        r=r+'1'
    else:
        r=r+'0'
    r=int(r, 2)
    s=str(r)+str(r%10)
    r=int(s)
    if r>1200:
        print(n, r)
        break
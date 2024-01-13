for i in range(1,1000):
    n=bin(i)[2:]
    if i%2==0:
        n='1'+n+str(n.count('1')%2)
    else:
        n = n + '0' + str(n.count('1') % 2)
    r=int(n,2)
    if r>100:
        print(r, i)
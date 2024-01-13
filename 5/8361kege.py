for i in range(1000, 0,-1):
    n=bin(i)[2:]
    if i%2!=0 and n.count('1')%2!=0:
        n='1'+n
    else:
        n=n + str(n.count('1')%2)
    if i%2!=0 and n.count('1')%2!=0:
        n='1'+n
    else:
        n=n + str(n.count('1')%2)
    if int(n,2)<100:
        print(i)
        break
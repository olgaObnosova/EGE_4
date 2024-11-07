for a in range(100):
    f=1
    for x in range(1000):
        f*=((x&a!=0) <=((x&17==0 and x&5==0) <= (x&3!=0)))
    if f:
        print(a)
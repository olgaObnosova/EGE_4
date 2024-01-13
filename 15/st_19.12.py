for a in range(1000):
    f=1
    for x in range(10000):
        f*=((x&57>0) or (x&99>0)) <= (x&a>0)
    if f:
        print(a)
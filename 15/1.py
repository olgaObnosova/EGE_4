for a in range(100):
    f=1
    for x in range(1000):
        f*=(x&9!=0 or x&19==0 or x&a!=0)
    if f:
        print(a)
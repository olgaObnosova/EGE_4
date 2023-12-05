for a in range(1,100):
    f=1
    for x in range(1,1000):
        f*=((x&103==0 and x&94!=0)<=(x&a!=0))
    if f:
        print(a)
        break
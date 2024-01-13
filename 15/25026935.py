for a in range(1,1000):
    f=1
    for x in range(200):
        for y in range(200):
            f*=(x>=27 or 2*x<3*y or (x+2)*(y-3)<a)
    if f:
        print(a)
        break
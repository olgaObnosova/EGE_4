for a in range(100, 1000):
    f=1
    for x in range(250):
        for y in range(250):
            f*=(11<=y or 7*y<x or a> x*y)
    if f:
        print(a)

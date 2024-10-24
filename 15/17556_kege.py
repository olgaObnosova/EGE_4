for a in range(1, 1000):
    f=1
    for x in range(1, 1000):
        f*=(x%a==0 or x not in range(70, 91) or x%22!=0)
    if f:
        print(a)

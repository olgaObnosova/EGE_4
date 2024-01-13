for n in range(100, 1000):
    a=(n%10)*(n//10%10) #23
    b=(n//100)*(n//10%10) #12
    minn=min(a, b)
    maxx=max(a, b)
    r = str(minn)+str(maxx)
    if int(r)==621:
        print(n)
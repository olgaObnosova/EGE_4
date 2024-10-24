for a in range(36,10,-1):
    s=int('lancelot', a)
    b=int('elsa', a)
    c=int('dragon', a)
    d=int('cat', a)
    if (s+b-c+d)%1747==0:
        print((s+b-c+d)//1747, a)
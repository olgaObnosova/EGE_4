for p in range(6, 50):
    for q in range(6, 20):
        a=2*p**4+4*p**3+3*p**2+5*p+1
        b=q**4+4*q**3+3*q**2+2*q+5
        if a==b:
            print(a, p, q)
for a in range(1, 5000):
    f=0
    for x in range(1, 5000):
        f+=((x%a!=0) or (x%2205!=0) or (x%2800==0))
    if f==0:
        print(a)

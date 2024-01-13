b = range(70, 81)
for a in range(500, 1,-1):
    f=0
    for x in range(1, 1000):
        f+=(x%12==0) and (x in b) and (x%a!=0)
    if not(f):
        print(a)
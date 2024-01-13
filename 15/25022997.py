c=range(30,46)
for a in range(1,100):
    f=1
    for x in range(1,10000):
        f*=(x%a!=0 or x not in c or x%12!=0)
    if f:
        print(a)
        break
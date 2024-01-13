def sem(i):
    s=''
    while i>0:
        s+=str(i%7)
        i=i//7
    return s[::-1]
for n in range(1, 10000):
    r=sem(n)
    per=r[0]
    posl=r[-1]
    r = posl + r[1:-1] +per
    r=int(r, 7)
    if r==2024:
        print(n)
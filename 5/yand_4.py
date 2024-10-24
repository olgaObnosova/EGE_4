def tr(n):
    s = ''
    while n != 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]


for i in range(1, 1000):
    n = tr(i)
    k2 = n.count('2')
    if k2==0:
        n = n + '0'
    else:
        n=n+tr(k2)
    k1 = n.count('1')
    if k1 == 0:
        n = n + '0'
    else:
        n=n+tr(k1)
    k0 = n.count('0')
    if k0==0:
        n = n + '0'
    else:
        n=n+tr(k0)
    r=int(n, 3)
    if r<1000:
        print(i)
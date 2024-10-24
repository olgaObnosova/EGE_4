def dv(n):
    s = ''
    alf = '0123456789ab'
    while n != 0:
        s += str(alf[n % 12])
        n //= 12
    return s[::-1]

minn=float('inf')
for i in range(1, 10000):
    n = dv(i)
    if i % 4 == 0:
        n = '2' + n + '64'
    else:
        n = n + max(n)
    r = int(n, 12)
    if r > 1799:
        minn=min(minn, r)
print(minn)
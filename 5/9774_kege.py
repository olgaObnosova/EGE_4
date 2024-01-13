def tr(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n = n // 3
    s = s[::-1]
    # print(s)
    return s

minn = float('inf')
for i in range(1, 1000):
    n = tr(i)
    if i % 3 == 0:
        n = n + n[-2:]
    else:
        ost = tr(i % 3 * 5)
        n = n + ost
    r = int(n, 3)
    if r > 133:
        minn = min(minn, r)
print(minn)

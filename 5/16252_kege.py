def f(h):
    s = ''
    while h != 0:
        s += str(h % 3)
        h = h // 3
    return s[::-1]

minn = 100000
for n in range(1, 1000):
    i = f(n)
    if n % 2 == 0:
        i = '2' + i + f(int(i[-1]) * 2)
    else:
        i = f(int(i[0]) * 2) + i + '2'
    r = int(i, 3)
    if 100 < r and r < minn:
        minn = r
print(minn)

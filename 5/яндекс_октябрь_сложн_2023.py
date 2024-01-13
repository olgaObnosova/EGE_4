def tr(i):
    s = ''
    while i > 0:
        s += str(i % 3)
        i = i // 3
    return s[::-1]


minn = 999999999
for n in range(1, 1000):
    r = tr(n)
    k = r.count('1') + r.count('2') * 2
    if len(r) % 2 != 0:
        r = '1' + r
    if k % 2 == 0:
        r = r + r[:2]
    else:
        ost = tr(n % 5)
        r = r + ost
    if r[0] == '2':
        r = r[1:]
    if r[-1] == r[-2]:
        r = r[:-1]
    r = int(r, 3)
    #print(r)
    if r > 150:
        minn=min(minn, r)
print(minn)

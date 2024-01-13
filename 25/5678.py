import fnmatch as f

for i in range(124579, 10 ** 8):
    if f.fnmatch(str(i), '124*5*79'):
        s = 0
        sc = 0
        for x in str(i):
            sc += int(x)
            if int(x) % 2 == 1:
                s += int(x)
        if i % s == 0:
            print(i, sc)

import fnmatch as f
for x in range(1996, 10**10 + 1, 1996):
    if f.fnmatch(str(x), '1592*6?8'):
        sr=str(x)[4:-3]
        fl=1
        for cif in sr: # 214
            if int(cif)%2!=0:
                fl=0
                break
        if fl:
            print(x, x//1996)
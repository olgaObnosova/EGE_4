def delit(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return list(s)


from fnmatch import *

for i in range(1, 10**9+1):
    if fnmatch(str(i), '15*3*09'):
        f = delit(i)
        if len(f) == 9:
            f.sort()
            print(i, f[-2])

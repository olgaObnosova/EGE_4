def pr(i):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

maxx=0

for a in range(36, 29, -1):
    for b in range(36, 28, -1):
        for y in range(36, 27, -1):
            for x in range(36, 29, -1):
                    k = int('lancelot', a)
                    l = int('elsa', b)
                    m = int('dragon', y)
                    n = int('cat', x)
                    if pr(k+l-m+n):
                        if a+b+y+x>maxx:
                            maxx=max(maxx, a+b+y+x)
                            otv=k+l-m+n
print(maxx)
print(otv)
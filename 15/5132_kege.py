def od(n, m):
    for i in range(2, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            return True
    return False


for a in range(1, 100):
    f = 1
    for x in range(1, 1000):
        f *= od(x, 42) <= (not (od(x, 7))) or (x + a >= 25)
    if f:
        print(a)
        break
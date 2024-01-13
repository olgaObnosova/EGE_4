for a in range(1, 2000):
    f = 1
    for x in range(1, 10000):
        f *= (((x % 175 == 0) <= (x % 25 != 0)) or (2 * x + a) >= 1780)
    if f:
        print(a)

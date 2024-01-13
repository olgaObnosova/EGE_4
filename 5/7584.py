for i in range(100):
    n = bin(i)[2:]
    if i % 3 == 0:
        n = n + n[-3:]
    else:
        d = bin(3 * (n % 3))[2:]
        n = n + d
    r = int(n, 2)
    if r < 100:
        print(i)


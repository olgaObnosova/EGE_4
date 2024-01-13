for a in range(100):
    for x in range(11):
        m = 4 * 12 ** 4 + 9 * 12 ** 3 + x * 12 ** 2 + 24 + 6
        n = 4 * 12 ** 4 + 9 * 12 ** 3 + x * 12 ** 2 + 7 * 12
        if (m + a) % n == 0:
            print(a, x)

for a in range(500):
    f = 1
    for x in range(1, 500):
        for y in range(1, 500):
            f *= (x + y <= 32 or y <= x + 4 or y >= a)
    if f:
        print(a)

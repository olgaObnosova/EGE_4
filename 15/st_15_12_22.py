for a in range(1, 100):
    f = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            f *= (144 % x != 0 or x % y != 0 \
                  or x + y > 100 or a - x > y)
    if f:
       print(a)
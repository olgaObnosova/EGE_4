for a in range(1, 500):
    f = 1
    for x in range(1, 1000):
        f *= (x % 2 != 0 or x % 3 != 0 \
              or x + a >= 100)
    if f:
        print(a)
        break

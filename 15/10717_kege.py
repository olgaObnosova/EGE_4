def tr(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


for a in range(200, 1, -1):
    f = 1
    for x in range(1, 1000):
        f *= not ((tr(x, 11, 18) == (max(x, 5) <= 68))\
                  and tr(x, a, 5))
    if f:
        print(a)
        break

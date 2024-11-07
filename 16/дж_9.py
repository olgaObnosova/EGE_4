def f(n):
    if n < 5:
        return n % 3
    elif n > 4 and n % 2 == 0:
        return 2 * f(n - 2) + n * 2
    elif n > 4 and n % 2 != 0:
        return f(n - 2) + n % 4
for i in range(1800, 1500, -1):
    d=f(i)
    if d<=1500:
        print(i, d)
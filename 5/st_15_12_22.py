def sch(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s % 2


for x in range(1000):
    y = bin(x)[2:]
    for i in range(3):
        n = int(y, 2)
        if sch(n):
            y = bin(n)[2:] + '1'
        else:
            y = bin(n)[2:] + '0'
    if int(y,2) > 1028:
        print(int(y,2), x)
        break

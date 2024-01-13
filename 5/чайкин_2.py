for i in range(100):
    n = i
    s = 0
    n = oct(n)[2:]
    ch = str(i)
    for x in ch:
        s+= int(x)
    if s % 2 == 0:
        n = n + str(i % 3)
    else:
        maxx = max([int(a) for a in n])
        n = str(maxx) + n
    if int(n, 8) > 127:
        print(i)
        break




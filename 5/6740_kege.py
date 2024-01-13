for i in range(9):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '01'
    r = int(n, 2)
    print(r)

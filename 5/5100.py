for i in range(1000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = n + '10'
    else:
        n = '1' + n + '01'
    n = int(n, 2)
    if n > 516:
        print(i)
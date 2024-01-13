for i in range(1, 1000):
    n = bin(i)[2:]
    if i % 11 == 0:
        n = n + n.count('0') * '0'
    else:
        n = n.count('1') * '1'+n
    if int(n, 2) % 227 == 0:
        print(i)
        break
print(2**12)
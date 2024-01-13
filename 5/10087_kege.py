m = float('inf')
for i in range(100):
    n = bin(i)[2:]
    if i % 3 == 0:
        n = n + n[-3:]
    else:
        s = bin(i % 3 * 3)[2:]
        n = n + s
    r = int(n, 2)
    if r > 151:
        m = min(r, m)
print(m)

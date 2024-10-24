m =99999999999999
for i in range(28, 10000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = n[2:]
        n = '10' + n + '0'
    else:
        n = n[2:]
        n = '11' + n + '1'
    n = int(n,2)
    m = min(m,n)
print(m)
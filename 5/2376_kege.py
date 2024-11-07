minn=float('inf')
for i in range(1,500):
    n = bin(i)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    r = int(n, 2)
    if r>60:
        minn=min(minn, r)
print(minn)

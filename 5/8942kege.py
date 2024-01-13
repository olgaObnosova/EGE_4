for i in range(10_000, 1, -1):
    n = bin(i)[2:]
    if n.count('1') % 4 == 0:
        n = '10' + n
    else:
        n = '11' + n
    if int(n,2)%2!=0:
        n = n + '0'
    else:
        n = n + '1'
    if int(n,2)<=250:
        print(i)
        break

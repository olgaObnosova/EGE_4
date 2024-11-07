def sem(n):
    s=''
    while n>0:
        s+=str(n%7)
        n=n//7
    return s[::-1]


for i in range(1, 1000000):
    n = sem(i)
    if n.count('2') % 2 == 0:
        n = n + '555'
    else:
        n = '1' + n
    r = int(n, 7)
    if r < 3799:
        print(i)
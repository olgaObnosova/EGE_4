def tru(n):
    s = ''
    while n!=0:
        ost = str(n%3)
        s = s + ost
        n = n // 3
    return s[::-1]
t = tru(25)
print(t)

m = 0
for i in range(1, 13):
    n = tru(i)[2:]
    if i % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '01'
    r = int(n, 2)
    m = max(m, r)
print(m)

def ch(n):
    s = ''
    while n != 0:
        s += str(n % 4)
        n = n // 4
    return s[::-1]


for i in range(1,1000):
    n = ch(i)
    dl = len(n)
    #print(n)
    if dl % 2 == 0: #1234
        n = n[:dl // 2] + '0' + n[dl // 2:]
    r = int(n) #333
    #print(n)
    if r <= 180:
        print(i)
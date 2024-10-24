def sh(n):
    s = ''
    while n != 0:
        s += str(n % 6)
        n = n // 6
    return s[::-1]
def pr(i):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            return False
    return True

minn=float('inf')
for i in range(100_000, 200_000):
    if pr(i):
        n = sh(i)
        n = n.replace('0', '!')
        n = n.replace('1', '@')
        n = n.replace('2', '#')
        n = n.replace('3', '$')
        n = n.replace('4', '%')
        n = n.replace('5', '1')
        n = n.replace('!', '3')
        n = n.replace('@', '5')
        n = n.replace('#', '4')
        n = n.replace('$', '0')
        n = n.replace('%', '2')
        if len(n)>0:
            n = int(n, 6)
            n = sh(n)
        n = n[::-1]
        if i%17==7:
            sm = sh(sum(map(int, str(n))))
            n = n + str(sm)
        if len(n)>0:
            r=int(n, 6)
            #print(r, i)
            if pr(r) and r>5*10**7:
                minn=min(minn, r)
print(minn)
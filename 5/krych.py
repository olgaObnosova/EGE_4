m = 9999999999999999999
def tru(n):
    k =''
    while n > 0:
        o = n % 5
        k = k + str(o)
        n = n // 5
    return k[::-1]
print(tru(108))
for i in range(7, 8):
    n = tru(i)
    if i % 5 == 0:
        n = n + '04'
    else:
        n = n + str((n.count('1')+ n.count('2')*2+\
                      n.count('3')*3+n.count('4') *4)*3)
    n = n[::-1]
    n = int(n)
    print(n)
    if n > 70:
        m = min(n,m)
print(m)
minn=9999999
for n in range(101, 1000):
    a='3'*n
    while '111' in a or '333' in a:
        if '111' in a:
            a=a.replace('111', '3')
        else:
            a=a.replace('333', '1')
    print(a, n)
    if int(a) < minn:
        minn = int(a)
        otv = n
print(otv)
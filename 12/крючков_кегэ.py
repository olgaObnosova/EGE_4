for n in range(1, 1000):
    a='5'*n
    while '34' in a or '55' in a:
        if '34' in a:
            a=a.replace('34','54321', 1)
        elif '55' in a:
                a=a.replace('55','234', 1)
    if 1000<len(str(a))<10_000:
        print(n)
        break
        
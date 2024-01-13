for n in range(4,100):
    a = '2' + n * '5'
    while '25' in a or '35' in a or '555' in a:
        if '25' in a:
            a=a.replace('25','53',1)
        if '35' in a:
            a = a.replace('35', '2', 1)
        if '25' in a:
            a = a.replace('555', '23', 1)
    s=0
    for x in a:
        s+=int(x)
    if s%7==0:
        print(n)
        break
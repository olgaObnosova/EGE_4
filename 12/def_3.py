for n in range(3, 10_000):
    a='5'+n*'2'
    while '52'in a or '2222' in a or '112' in a:
        if '52' in a:
            a=a.replace('52', '11',1)
        if '2222' in a:
            a = a.replace('2222', '5', 1)
        if '112' in a:
            a = a.replace('112', '25', 1)
    s=0
    for x in a:
        s+=int(x)
    if s==2024:
        print(n)

for n in range(1,100):
    a='>'+21*'0'+n*'1'+11*'2'
    while '>1' in a or '>2' in a or'>0' in a:
        if '>1' in a:
            a=a.replace('>1','22>',1)
        if '>2' in a:
            a=a.replace('>2','2>',1)
        if '>0' in a:
            a=a.replace('>0','1>',1)
    s=0
    for x in a:
        if x!='>':
            s+=int(x)
    if s%n==0:
        print(n)
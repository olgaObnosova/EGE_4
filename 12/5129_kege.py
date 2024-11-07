for n in range(100):
    a = '>' + 15 * '1' + n * '2' + 16 * '3'
    while '>1' in a or '>2' in a or '>3' in a:
        if '>1' in a:
            a=a.replace('>1', '22>', 1)
        if '>3' in a:
            a = a.replace('>3', '13>', 1)
        if '>2' in a:
            a = a.replace('>2', '1000>3', 1)
    s=0
    for x in a: #123>
        if x!='>':
            s+=int(x)
    if s % len(a)==0:
        print(n)

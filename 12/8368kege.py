for n in range(99,9,-1):
    a='3'+n*'7'
    while '37' in a or '577' in a or '777' in a:
        if '37' in a:
            a=a.replace('37','7',1)
        if '577' in a:
            a=a.replace('577','73',1)
        if '777' in a:
            a=a.replace('777','5',1)
    s=0
    for x in a:
        s+=int(x)
    print(s, n)

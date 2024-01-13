for i in range(101,1000):
    a='3'*i
    while '111' in a or '333' in a:
        if '111' in a:
            a=a.replace('111','3',1)
        else:
            a=a.replace('333','1',1)
    print(a,i)
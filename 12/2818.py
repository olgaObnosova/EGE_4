for i in range(31,100):
    a=i*'1'
    while '111' in a:
        a=a.replace('111','2',1)
        a=a.replace('222','1',1)
    if a=='211':
        print(i)
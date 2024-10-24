for x in '0123456789abcd':
    for y in '0123456789abcd':
        a = int(f'14{y}5{x}2', 14)
        b = int(f'31{x}2{y}3', 14)
        if (a+b)%9==0:
            print(a+b, x, (a+b)/9)
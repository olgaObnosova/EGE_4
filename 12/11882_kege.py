for n in range(3, 10000):
    a='5'+'2'*n
    while '52' in a or '2222' in a or '1122' in a:
        if '52' in a:
            a=a.replace('52', '11')
        if '2222' in a:
            a=a.replace('2222', '5')
        if '1122' in a:
            a=a.replace('1122', '25')
    k=a.count('1')+a.count('2')*2+a.count('5')*5
    if k==64:
        print(n)
print(bin(192),bin(168), bin(160), bin(240))
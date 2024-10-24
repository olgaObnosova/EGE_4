for n in range(1, 100):
    a = '1' * 40 +  '3' * n + '2' * 40
    while '23' in a or '12' in a or '32' in a:
        if '12' in a:
            a = a.replace('12', '21', 1)
        if '32' in a:
            a = a.replace('32', '1', 1)
        if '23' in a:
            a = a.replace('23', '2', 1)
    k = a.count('1') + a.count('2') * 2 + a.count('3') * 3
    if k == 100:
        print(n)
        break
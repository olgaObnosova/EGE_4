a = '0' + 9 * '1'+'21'+9*'2' + '0'
while not '00' in a:
    a = a.replace('012', '30')
    if '011' in a:
        a = a.replace('011', '20', 1)
        a = a.replace('022', '40', 1)
    else:
        a = a.replace('01', '10', 1)
        a = a.replace('02', '101', 1)
print(a)

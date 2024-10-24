n = '1' + 105 * '0'
while '1' in n:
    if '100' in n:
        n = n.replace('100', '0001', 1)
    else:
       n =  n.replace('1', '00', 1)
print(n.count('0'))
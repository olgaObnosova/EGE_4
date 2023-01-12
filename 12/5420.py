a = 197*'1'+'2' + 6 * '1'
while '111' in a or '222' in a:
    if '111' in a:
        a = a.replace('111', '22', 1)
    else:
        a = a.replace('222', '11', 1)
print(a)

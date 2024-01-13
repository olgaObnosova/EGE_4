k=0
for x1 in '1234567':
    for x2 in '01234567':
        for x3 in '01234567':
            for x4 in '01234567':
                for x5 in '01234567':
                    x = x1 + x2 + x3 + x4 + x5
                    if x.count('6') == 1 and '16' not in x \
                            and '61' not in x and '36' not in x \
                            and '63' not in x and '56' not in x and \
                            '65' not in x and '76' not in x and \
                            '67' not in x:
                        k+=1
print(k)

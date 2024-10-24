k=0
for x1 in '123':
    for x2 in '0123':
        for x3 in '0123':
            for x4 in '0123':
                for x5 in '0123':
                    a = x1+x2+x3+x4+x5
                    if a.count('3')==1 and '00' not in a and\
                        '11' not in a and '22' not in a:
                        k+=1
print(k)

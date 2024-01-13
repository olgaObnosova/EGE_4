k=0
for x1 in 'СПОРТЛ':
    for x2 in 'СПРТЛО':
        for x3 in 'СПРТЛО':
            for x4 in 'СПРТЛО':
                for x5 in 'СПРТЛО':
                    for x6 in 'СПРТЛО':
                        for x7 in 'СПРТЛО':
                            for x8 in 'СПРТЛО':
                                for x9 in 'СПРТЛО':
                                    s = x1+x2+x3+x4+x5+x6+x7+x8+x9
                                    if s.count('С')==1 and s.count('П')==1 and \
                                            s.count('О') == 3 and s.count('Р')==1 and \
                                            s.count('Т') == 2 and s.count('Л')==1 and\
                                            'ОО' in s:
                                        k+=1

print(k)

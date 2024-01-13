alf = 'АЕИКМНХ'
q = 0
w = ''
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        for i7 in alf:
                            s = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            if s == 'АНИМЕКХ':
                                w = 'АНИМЕКХ'
                            if s == 'МЕХАНИК':
                                w = 'МЕХАНИК'
                            if w == 'АНИМЕКХ': #ХМ МХ ММ ХК
                                if s.count('М'):
                                    s = s.replace('Х','*')
                                    s = s.replace('Н', '*')
                                    s = s.replace('К', '*')
                                    if 'ММ' not in s and 'М*' not in s\
                                            and '*М' not in s:
                                        q+=1
                                    '''
                                    e = 0
                                    for x in range(len(s) - 1):
                                        if s[x] == 'М':
                                            if s[x + 1] not in 'МХНК' and s[x - 1] not in 'МХНК':
                                                e += 1
                                    if s[-1] == 'М':
                                        if s[-2] not in 'МХНК':
                                            e += 1
                                    if e == s.count('М'):
                                        q += 1
                                        '''
print(q)
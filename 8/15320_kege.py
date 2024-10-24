k=0
for x1 in 'апрсу':
    for x2 in 'апрсу':
        for x3 in 'апрсу':
            for x4 in 'апрсу':
                for x5 in 'апрсу':
                    sl=x1+x2+x3+x4+x5
                    k+=1
                    if sl.count('у')<2 and 'аа' not in sl:
                        print(k)
                        break

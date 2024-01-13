k=0
for x1 in 'АПРСУ':
    for x2 in 'АПРСУ':
        for x3 in 'АПРСУ':
            for x4 in 'АПРСУ':
                for x5 in 'АПРСУ':
                    x=x1+x2+x3+x4+x5
                    k+=1
                    if x[0]=='У' and 'АА' not in x:
                        print(k)
                        break
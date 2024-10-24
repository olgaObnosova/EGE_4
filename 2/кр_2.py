print('n a d g r o')
for n in 0,1:
    for a in 0, 1:
        for d in 0, 1:
            for g in 0, 1:
                for r in 0, 1:
                    for o in 0, 1:
                        if ((((d and r) or a) <=g) \
                                and (o or (n and d))) and \
                                ((r!=(a and g)) and not(o<=n)):
                            print(n,a,d,g,r,o)
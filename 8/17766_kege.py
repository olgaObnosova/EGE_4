x='бенрстья'
k=0
for x1 in x:
    for x2 in x:
        for x3 in x:
            for x4 in x:
                for x5 in x:
                    k=k+1
                    a=x1+x2+x3+x4+x5
                    if k%2==0 and a[0]=='р' \
                            and 'ь' not in a:
                        print(k, a)


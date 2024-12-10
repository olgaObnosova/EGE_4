sp='0123456789abcde'
k=0
for x1 in sp:
    for x2 in sp:
        for x3 in sp:
            for x4 in sp:
                for x5 in sp:
                    for x6 in sp:
                        for x7 in sp:
                            for x8 in sp:
                                x=x1+x2+x3+x4+x5+x6+x7+x8
                                if x[0]=='0':
                                    continue
                                k+=1
print(k)




c='012345678'
k=0
for x1 in c:
    for x2 in c:
        for x3 in c:
            for x4 in c:
                for x5 in c:
                    a= x1+x2+x3+x4+x5
                    if a[0]!='0' and a.count('5')==1\
                        and '00' not in a and '11' not in a \
                            and '22' not in a and '33' not in a \
                            and '44' not in a and '55' not in a \
                            and '66' not in a and '77' not in a \
                            and '88' not in a:

                        k+=1
print(k)
print(3**3*2**2+3*4*2*3)


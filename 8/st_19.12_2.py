ch='2468'
n='1357'
k=0
for x1 in n:
    for x2 in ch:
        for x3 in n:
            for x4 in ch:
                for x5 in n:
                    for x6 in ch:
                        for x7 in n:
                            for x8 in ch:
                                for x9 in n:
                                    for x10 in ch:
                                        for x11 in n:
                                            x =x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11
                                            if x.count('1')<=4 and x.count('2')<=4 and x.count('3')<=4 and \
       x.count('4')<=4 and x.count('5')<=4 and x.count('6')<=4 and \
       x.count('6')<=4 and x.count('7')<=4 and x.count('8')<=4:
                                                k+=1

print(k)
print(4100400*2)
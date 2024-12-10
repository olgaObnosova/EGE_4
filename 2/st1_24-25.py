print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if  ((1-x) or (1-y) or z)\
                        and ((1-y) or(z!=w))==0:
                    print(x,y,z,w)#
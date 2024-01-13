print('x,y,z,w')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not(z or not(w<=x) or (z or not(y))):
                    print(x,y,z,w)
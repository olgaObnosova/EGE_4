print('x y z w u')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                for u in 0, 1:
                    if not(((x<=y) and(z!=w))<=(u==(x or z))):
                        print(x,y,z,w,u)
print('x,y,z,w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                a = (x != y) <= ((z <= (1-w)) and (w <= y))
                print(x, y, z, w, a)

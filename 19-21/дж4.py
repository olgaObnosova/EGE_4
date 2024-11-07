def f(a, h, ph):
    if a  == 1:
        return h % 2 == ph % 2
    elif h == ph:
        return 0
    pos = [f(a //2+1,  h + 1, ph),f(a //2,  h + 1, ph),\
           f(a //2+2,  h + 1, ph)]

    return any(pos) if (h + 1) % 2 == ph % 2 else all(pos)

k=0
for a in range(9,0,-1):
    if f(a, 0, 3):
        print(a)



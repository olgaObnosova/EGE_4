def f(a,b, h, ph):
    if a**2+b**2 >= 13**2:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a + 3,b, h + 1, ph), f(a,b+3, h+1,ph),\
            f(a ,b+4, h + 1, ph)]
    return any(comb) if (h + 1) % 2 == ph % 2\
        else all(comb)
for a in range(1,13):
        for ph in range(5):
            if f(a,2,0,ph):
                if ph==4:
                    print(a,ph)
                break